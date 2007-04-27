#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb
from datetime import *
import configurables

global form
form = cgi.FieldStorage()

global host
global database
global user
global passwd

host = configurables.host()
database = configurables.db()
user = configurables.user()
passwd = configurables.passwd()

def lookup():
	
	try:
		
		ms = MySQLdb.connect(host,user,passwd,database)
		cur = ms.cursor()
		cur.execute("""select * from Users where UID=%s""",(form.getvalue("skew")))
		x = cur.fetchall()
		ms.close()
		#if len(x) == 0:
		#	raise NameError
	
		print "Content-Type: text/html\n\n"
		print "<HTML>\n<HEAD>"
		print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
		print "\t<TITLE> UID found!</TITLE>\n"
		print "</HEAD>\n<BODY>\n"
		
		print "<FORM METHOD = post ACTION = \"/cgi-bin/user-modify.cgi\">"
		if str(x) == "()":
			raise NameError
		UID = str(x[0][0])
		while len(UID) < 9:
			UID = "0" + UID 
			
		print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
		print "\t<tr>"
		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
		print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Personal Information:</b></font></td>"
	
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
		print "\t\t<input type=\"hidden\" name=\"selection\" value=\"mod\">"
		print "\t\t<input type=\"hidden\" name=\"skew\" value=\"%s\">"%(form.getvalue("skew"))
		
		print "\t\tPrefix:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][1] =="":
			print "<input type=\"text\" name=\"prefix\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%("")
			
		else:
			print "<input type=\"text\" name=\"prefix\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][1])
		
	
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tFirst Name:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "<input type=\"text\" name=\"f_name\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][2])
			
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tMiddle Name:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][3] =="":
			print "<input type=\"text\" name=\"m_name\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%("")
		else:
			print "<input type=\"text\" name=\"m_name\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][3])
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tLast Name:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "<input type=\"text\" name=\"l_name\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][4])
			
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tSuffix:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][5] =="":
			print "<input type=\"text\" name=\"suffix\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%("")
		else:
			print "<input type=\"text\" name=\"suffix\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][5])
		
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
		print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Contact Information:</b></font></td>"
	
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tHome Phone Number:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][6] =="":
			print "<input type=\"text\" name=\"h_ph\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%("(none provided)")
		else:
			print "<input type=\"text\" name=\"h_ph\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][6])

	
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tCell Phone Number:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][7] =="":
			print "<input type=\"text\" name=\"c_ph\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%("(none provided)")
		else:
			print "<input type=\"text\" name=\"c_ph\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][7])
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tWork Phone Number:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][8] =="":
			print "<input type=\"text\" name=\"w_ph\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%("(none provided)")
		else:
			print "<input type=\"text\" name=\"w_ph\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][8])
		
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tEmail Address:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][9] =="":
			print "<input type=\"text\" name=\"email\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%("(none provided)")
		else:
			print "<input type=\"text\" name=\"email\" size=\"30\" maxlength=\"40\" value=\"%s\"></td>"%(x[0][9])

		
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tPostal Address:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][10] =="":
			print "\t\t<textarea name=\"address\" cols=30 rows =1>%s</textarea></td>"%("(none provided)")
		else:
			print "\t\t<textarea name=\"address\" cols=30 rows =1>%s</textarea></td>"%(x[0][10])
		
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
		print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Account Information:</b></font></td>"
		
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tUser ID Number:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "\t\t%s</td>"%(UID)
	
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tLast Modified:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "\t\t%s</td>"%(x[0][11].strftime("%Y-%m-%d %H:%M:%S"))
	
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tExpiration:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "\t\t%s</td>"%(x[0][12].strftime("%Y-%m-%d %H:%M:%S"))
		#tim = x[0][12].strftime("%Y-%m-%d %H:%M:%S")
		#tim = tim.split(" ")
		#tim[0] = tim[0].split("-")	
		#tim[1] = tim[1].split(":")	
		#print "<select name=\"year\">\n"
	
	
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tCurrent Status:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "<select name=\"status\">\n"
		if str(x[0][13]) == "Set([\'Active\'])" or str(x[0][13]) == "Active":
			print "<option>Active\n<option>Suspended\n<option>Expired\n<option>Delete\n"
			
		elif str(x[0][13]) == "Set([\'Suspended\'])" or str(x[0][13]) == "Suspended":
			print "<option>Suspended\n<option>Active\n<option>Expired\n<option>Delete\n"
	
		elif str(x[0][13]) == "Set([\'Expired\'])" or str(x[0][13]) == "Expired":
			print "<option>Expired\n<option>Active\n<option>Suspended\n<option>Delete\n"
		
		else:
			print "<option>Delete\n"
		print "</select></td>\n"
		
		print "\t<tr>\n"
    		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\" align=\"center\">"
    		
    		if str(x[0][13]) == "Set([\'Deleted\'])" or str(x[0][13]) == "Deleted":
    			print "\t\t\t[Submit]"
    		else:
    			print "\t\t\t<INPUT TYPE = submit VALUE = \"Submit\">"
		print "\t\t</td>"
		print "\t</tr>"
		
		print "\t</tr>\n</table>\n</FORM>\n</BODY>\n</HTML>"
		
		
	except:
		error()

def modify():
	try:
		
		
		if form.getvalue("status") == "Delete":
			ms = MySQLdb.connect(host,user,passwd,database)
			cur = ms.cursor()
			ct = datetime.today()
			ct = ct.strftime( "%Y-%m-%d %H:%M:%S" )
			#cur.execute("""DELETE FROM Users WHERE UID=%s""",(form.getvalue("skew")))
			cur.execute("""UPDATE Users SET Modify=%s, Expire=%s, Status=%s WHERE UID=%s""",(ct,ct,"Deleted",form.getvalue("skew")))
			
			ms.close()
			
			print "Content-Type: text/html\n\n"
			print "<HTML>\n<HEAD>"
			print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
			print "\t<TITLE>1</TITLE>\n"
			print "</HEAD>\n<BODY>"  
			print "<h1>Success!</h1>"
			print "User %s has been deleted.<br>"%form.getvalue("skew")
			print "(Well, not really.  The Status has been set to \"Deleted\" because deletion is not implemented in this version."
			print "</BODY>\n</HTML>"
			
		else:
			ct = datetime.today()
			ct = ct.strftime( "%Y-%m-%d %H:%M:%S" )
			prefix = ""
			suffix = ""
			h_ph = ""
			c_ph = ""
			w_ph = ""
			email = ""
			address = "" 
			
					
			if form.getvalue("prefix"):
				prefix = form.getvalue("prefix")
			if form.getvalue("suffix"):
				prefix = form.getvalue("suffix")
			if form.getvalue("h_ph") == "(none provided)":
				pass
			else:
				h_ph = form.getvalue("h_ph")
			if form.getvalue("c_ph") == "(none provided)":
				pass
			else:
				c_ph = form.getvalue("c_ph")
			if form.getvalue("w_ph") == "(none provided)":
				pass
			else:
				w_ph = form.getvalue("w_ph")
			if form.getvalue("email") == "(none provided)":
				pass
			else:
				email = form.getvalue("email")
			if form.getvalue("address") == "(none provided)":
				pass
			else:
				address = form.getvalue("address")
				
			ms = MySQLdb.connect(host,user,passwd,database)
			
			cur = ms.cursor()
			cur.execute("""UPDATE Users SET Prefix=%s,F_Name=%s,M_Name=%s,L_Name=%s,Postfix=%s,H_PH=%s, C_PH=%s, W_PH=%s, Email=%s, Address=%s, Status=%s, Modify=%s WHERE UID=%s""",(prefix,form.getvalue("f_name"),form.getvalue("m_name"),form.getvalue("l_name"),suffix,h_ph,c_ph,w_ph,email,address,form.getvalue("status"),ct,form.getvalue("skew")))
			cur.execute("""SELECT * FROM Users WHERE UID=%s""",(form.getvalue("skew")))
			x = cur.fetchall()
			
			ms.close()
			
			print "Content-Type: text/html\n\n"
			print "<HTML>\n<HEAD>\n"
			print "\t<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
			print "\t<TITLE>User Modified Successfully</TITLE>\n"
			print "</HEAD>\n<BODY>"
			print "<h1>User Has Been Modified Successfully!</h1>"
			
			
			print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
			print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
			print "\t<tr>"
			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Personal Information:</b></font></td>"
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
			print "\t\tPrefix:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][1] =="":
				print "\t\t&nbsp;</td>"
			else:
				print "\t\t%s</td>"%(x[0][1])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tFirst Name:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(x[0][2])
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tMiddle Name:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][3] =="":
				print "\t\t&nbsp;</td>"
			else:
				print "\t\t%s</td>"%(x[0][3])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tLast Name:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(x[0][4])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tSuffix:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][5] =="":
				print "\t\t&nbsp;</td>"
			else:
				print "\t\t%s</td>"%(x[0][5])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Contact Information:</b></font></td>"
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tHome Phone Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][6] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(x[0][6])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tCell Phone Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][7] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(x[0][7])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tWork Phone Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][8] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(x[0][8])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tEmail Address:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][9] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(x[0][9])
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tPostal Address:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][10] =="":
				print "\t\t(none provided)</td>"
			else:
				print "\t\t%s</td>"%(x[0][10])
		
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Account Information:</b></font></td>"
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tUser ID Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(form.getvalue("skew"))
			
			print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%(form.getvalue("skew"))
			print "<input type=\"hidden\" name=\"type\" value=\"B\">"
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tLast Modified:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(x[0][11].strftime("%Y-%m-%d %H:%M:%S"))
	
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tExpiration:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(x[0][12].strftime("%Y-%m-%d %H:%M:%S"))
			
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tCurrent Status:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
	
			if str(x[0][13]) == "Set([\'Active\'])":
				print "\t\tActive</td>"
			elif str(x[0][13]) == "Set([\'Expired\'])":
				print "\t\tExpired</td>"
			elif str(x[0][13]) == "Set([\'Suspended\'])":
				print "\t\tSuspended</td>"
			elif str(x[0][13]) == "Set([\'Deleted\'])":
				print "\t\tDeleted</td>"
			else:
				print "\t\t%s</td>"%(str(x[0][13]))
			print "</tr><tr>"
			print "<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\" align=\"center\">"
    			print "<select name=\"ht\">\n"
    			print "<option>Full<option>Half"
    			print "</select>\n"
    			print "<INPUT TYPE = submit VALUE = \"Generate Barcode\">"
			print "</td>"
			print "\t</tr>\n</table>\n</form>\n</BODY>\n</HTML>"
			
			
	except:
		error()

def error():
	print "Content-Type: text/html\n\n"
	print "<HTML>\n<HEAD>"
	print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
	print "\t<TITLE> UID not found!</TITLE>\n"
	print "</HEAD>\n<BODY>"  
	print "<h1>Error: User Not Found!</h1>"
	print "Sorry, but the User ID is invalid."
	print "</BODY>\n</HTML>"

if form.getvalue("selection") == "initial":
	lookup()
elif form.getvalue("selection") == "mod":
	modify()
else:
	error()
