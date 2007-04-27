#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb
import configurables
from datetime import *

form = cgi.FieldStorage()

host=configurables.host()
database=configurables.db()
user = configurables.user()
passwd = configurables.passwd()

uid = "%"
f_name = "%"
m_name = "%"
l_name = "%"
prefix = "%"
suffix = "%"
h_ph = "%"
c_ph = "%"
w_ph = "%"
email = "%"
address = "%"
status = "%"

try:
	if form.getvalue("skew"):
		uid = form.getvalue("skew")
	if form.getvalue("prefix"):
		prefix = form.getvalue("prefix")
	if form.getvalue("f_name"):
		f_name = form.getvalue("f_name") + f_name
	if form.getvalue("m_name"):
		m_name = form.getvalue("m_name") + m_name
	if form.getvalue("l_name"):
		l_name = form.getvalue("l_name") + l_name
	if form.getvalue("suffix"):
		suffix = form.getvalue("suffix")
	if form.getvalue("h_ph"):
		h_ph = form.getvalue("h_ph") + h_ph
	if form.getvalue("c_ph"):
		c_ph = form.getvalue("c_ph") + c_ph
	if form.getvalue("w_ph"):
		w_ph = form.getvalue("w_ph") + w_ph
	if form.getvalue("email"):
		email = form.getvalue("email") + email
	if form.getvalue("address"):
		address = form.getvalue("address") + address
	if form.getvalue("status"):
		status = form.getvalue("status")
	if form.getvalue("status") == "Any":
		status = "%"
	
	
	ms = MySQLdb.connect(host,user,passwd,database)
	cur = ms.cursor()
	cur.execute("""SELECT * FROM Users WHERE UID LIKE %s AND Prefix LIKE %s AND F_Name LIKE %s AND M_Name LIKE %s AND L_Name LIKE %s AND Postfix LIKE %s AND H_PH LIKE %s AND C_PH LIKE %s AND W_PH LIKE %s AND Email LIKE %s AND Address LIKE %s AND Status LIKE %s""",(uid,prefix,f_name,m_name,l_name,suffix,h_ph,c_ph,w_ph,email,address,status))
	x = cur.fetchall()
	ms.close()
	
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"	
	
	if len(x) == 0:
		print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
		print "\t<tr>"
		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
		print "\t\t<font color=\"#FFFFFF\"><center><h1>Sorry.  No Records Found.</h1></center></font></td>"
		print "\t</tr>\n\t<tr>"
		print "\n</table>\n"
	
	else:
		
		for g in x:	
			UID = str(g[0])
			while len(UID) < 9:
				UID = "0" + UID
			print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
			print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
			print "\t<tr>"
			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			print "\t\t<font color=\"#FFFFFF\"><h1>User: %s</h1></font></td>"%(UID)
			print "\t</tr>\n\t<tr>"

			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Personal Information:</b></font></td>"
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
			print "\t\tPrefix:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if g[1] =="":
				print "\t\t&nbsp;</td>"
			else:
				print "\t\t%s</td>"%(g[1])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tFirst Name:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(g[2])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tMiddle Name:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if g[3] =="":
				print "\t\t&nbsp;</td>"
			else:
				print "\t\t%s</td>"%(g[3])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tLast Name:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(g[4])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tSuffix:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if g[5] =="":
				print "\t\t&nbsp;</td>"
			else:
				print "\t\t%s</td>"%(g[5])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Contact Information:</b></font></td>"
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tHome Phone Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if g[6] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(g[6])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tCell Phone Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if g[7] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(g[7])
		
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tWork Phone Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if g[8] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(g[8])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tEmail Address:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if g[9] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(g[9])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tPostal Address:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if g[10] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(g[10])
		
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Account Information:</b></font></td>"
		
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tUser ID Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(UID)
			
			print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%(UID)
			print "<input type=\"hidden\" name=\"type\" value=\"B\">"
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tLast Modified:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(g[11].strftime("%Y-%m-%d %H:%M:%S"))
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tExpiration:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(g[12].strftime("%Y-%m-%d %H:%M:%S"))
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tCurrent Status:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	
			if str(g[13]) == "Set([\'Active\'])":
				print "\t\tActive</td>"
			elif str(g[13]) == "Set([\'Expired\'])":
				print "\t\tExpired</td>"
			elif str(g[13]) == "Set([\'Suspended\'])":
				print "\t\tSuspended</td>"
			elif str(g[13]) == "Set([\'Deleted\'])":
				print "\t\tDeleted</td>"
			else:
				print "\t\t%s</td>"%(str(g[13]))
				
			print "</tr><tr>"
    			print "<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\" align=\"center\">"
   		 	print "<select name=\"ht\">\n"
   		 	print "<option>Full<option>Half"
   		 	print "</select>\n"
  		  	print "<INPUT TYPE = submit VALUE = \"Generate Barcode\">"
			print "</td>"
	
			print "\t</tr>\n</table>\n</form>\n<br>\n"
			
	print "</BODY>\n</HTML>"
	
except:

	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>\n"
	print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE></TITLE>\n"
	print "</HEAD>\n<BODY>"
	print "<h1>An Error Was Encountered.</h1>"
	print "Please check to see if the for was correctly filled out.<br>"
	print "If this problem continues, please contact your administrator."
	print "</BODY>\n</HTML>"
	      ;  ��	                         ����    ����        ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������R o o t   E n t r y                                               ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                                    ����                                                                            ������������                          