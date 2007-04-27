#!/usr/bin/python
import MySQLdb

print "CITEP Bar Code System Installer"
print "I am going to ask you a series of questions.\nSuggested values will be noted in [brackets]."
host = raw_input("What is the host name of your MySQL server? [127.0.0.1] ")
if host == "":
    host = "localhost"
user = raw_input("What is the user name you wish to use for the install? [root] ")
if user =="":
    user="root"
passwd = raw_input("What is the password for the user ID you provided in the last question? ")
try:
    print "Connecting to database..."
    ms = MySQLdb.connect(host,user,passwd)
    cur = ms.cursor()
    print "Creating Database..."
    cur.execute("""CREATE DATABASE IF NOT EXISTS barcode""")
    cur.execute("""USE barcode""")
    cur.execute("""DROP TABLE IF EXISTS `Items`;""")
    cur.execute("""DROP TABLE IF EXISTS `Transactions`;""")
    cur.execute("""DROP TABLE IF EXISTS `Users`;""")
    cur.execute("""CREATE TABLE `Items` (`Class` set('I','S') NOT NULL,`IID` bigint(8) unsigned zerofill NOT NULL auto_increment,`Description` text NOT NULL,`Owner` text,`Status` set('Active','Inactive','Expired') NOT NULL default 'Active',PRIMARY KEY  (`Class`,`IID`)) ENGINE=MyISAM DEFAULT CHARSET=utf8;""") 
    cur.execute("""CREATE TABLE `Transactions` (`Class` set('T') NOT NULL default 'T',`TID` bigint(8) unsigned zerofill NOT NULL auto_increment,`Date` datetime NOT NULL default '0000-00-00 00:00:00',`UID` bigint(9) unsigned zerofill NOT NULL,`Items` text NOT NULL,PRIMARY KEY  (`Class`,`TID`)) ENGINE=MyISAM DEFAULT CHARSET=utf8;""")
    print "Creating configuration file..."
    f = open('cgi-bin/configurables.py', 'w')
    output = "def host():\n\treturn \"%s\"\ndef db():\n\treturn \"barcode\"\ndef user():\n\treturn \"%s\"\ndef passwd():\n\treturn \"%s\"\n"%(host,user,passwd)
    f.write(output)
    f.close()
    
    cur.execute("""CREATE TABLE `Users` (`UID` bigint(9) unsigned zerofill NOT NULL auto_increment,`Prefix` text,`F_Name` text NOT NULL,`M_Name` text,`L_Name` text NOT NULL,`Postfix` text,`H_PH` text,`C_PH` text,`W_PH` text,`Email` text,`Address` text,`Modify` datetime NOT NULL default '0000-00-00 00:00:00',`Expire` datetime NOT NULL default '0000-00-00 00:00:00',`Status` set('Active','Expired','Suspended','Deleted') NOT NULL default 'Active',PRIMARY KEY  (`UID`)) ENGINE=MyISAM DEFAULT CHARSET=utf8;""")
    ms.close()
    print "The database has been created :-D"
except:
    print "Something Failed! :-("
print "The Citep Bar Code System Installer is now exiting."