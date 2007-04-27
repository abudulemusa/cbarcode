#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb
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
	itemclass = ""
	iid = ""
	try:
		if form.getvalue("skew"):
			itemclass = form.getvalue("skew")[0]
			iid = form.getvalue("skew")[1:9]
			
		ms = MySQLdb.connect(host,user,passwd,database)
		cur = ms.cursor()
		cur.execute("""select * from Items where Class=%s AND IID=%s""",(itemclass,iid))
		x = cur.fetchall()
		ms.close()
		if len(x) == 0:
			raise NameError
	
		print "Content-Type: text/html\n\n"
		print "<HTML>\n<HEAD>"
		print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
		print "\t<TITLE> IID not found!</TITLE>\n"
		print "</HEAD>\n<BODY>\n"
		print "<FORM METHOD = post ACTION = \"/cgi-bin/item-modify.cgi\">"
		print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
		print "\t<tr>"
		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
		if str(x[0][0]) == "S" or str(x[0][0])=="Set([\'S\'])":
				print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Service Information:</b></font></td>"
		else:
				print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Item Information:</b></font></td>"
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
		print "\t\tItem Identificaiton Number:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "\t\t%s</td>"%(form.getvalue("skew"))
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tDescription:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "\t\t<input type=\"hidden\" name=\"selection\" value=\"mod\">"
		print "\t\t<input type=\"hidden\" name=\"skew\" value=\"%s\">"%(form.getvalue("skew"))
		print  "\t\t<textarea name=\"desc\" cols=30 rows =1>%s</textarea></td>"%(x[0][2])
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tOwner:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		if x[0][3] =="":
			print "\t\t<textarea name=\"owner\" cols=30 rows =1>%s</textarea></td>"%("(none provided)")
		else:
			print  "\t\t<textarea name=\"owner\" cols=30 rows =1>%s</textarea></td>"%(x[0][3])
		print "\t</tr>\n\t<tr>"
		print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
		print "\t\tStatus:</td>"
		print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
		print "<select name=\"status\">\n"
		if str(x[0][4]) == "Set([\'Active\'])" or str(x[0][4]) == "Active":
			print "<option>Active\n<option>Inactive\n<option>Expired\n<option>Delete\n"
			
		elif str(x[0][4]) == "Set([\'Inactive\'])" or str(x[0][4]) == "Inactive":
			print "<option>Inactive\n<option>Active\n<option>Expired\n<option>Delete\n"
	
		elif str(x[0][4]) == "Set([\'Expired\'])" or str(x[0][4]) == "Expired":
			print "<option>Expired\n<option>Active\n<option>Inactive\n<option>Delete\n"
		
		else:
			print "<option>Active\n<option>Inactive\n<option>Expired\n<option>Delete\n"
		print "</select></td>\n"
		print "\t<tr>\n"
    		print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\" align=\"center\">"
    		print "\t\t\t<INPUT TYPE = submit VALUE = \"Submit\">"
		print "\t\t</td>"
		print "\t</tr>"
		
		print "\t</tr>\n</table>\n</FORM>\n</BODY>\n</HTML>"
	except:
		error()

def modify():
	try:
		itemclass = ""
		iid = ""
		if form.getvalue("skew"):
			itemclass = form.getvalue("skew")[0]
			iid = form.getvalue("skew")[1:9]
		
		if form.getvalue("status") == "Delete":
			ms = MySQLdb.connect(host,user,passwd,database)
			cur = ms.cursor()
			cur.execute("""DELETE FROM Items WHERE Class=%s AND IID=%s""",(itemclass,iid))
			ms.close()
			
			print "Content-Type: text/html\n\n"
			print "<HTML>\n<HEAD>"
			print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
			print "\t<TITLE>1</TITLE>\n"
			print "</HEAD>\n<BODY>"  
			print "<h1>Success!</h1>"
			print "Item %s has been deleted."%form.getvalue("skew")
			print "</BODY>\n</HTML>"
			
		else:
			owner = ""
			if not form.getvalue("owner") == "(none provided)":
				owner = form.getvalue("owner")
			
			ms = MySQLdb.connect(host,user,passwd,database)
			cur = ms.cursor()
			cur.execute("""UPDATE Items SET Description=%s, Owner=%s, Status=%s WHERE Class=%s AND IID=%s""",(form.getvalue("desc"),owner,form.getvalue("status"),itemclass,iid))
			cur.execute("""select * from Items where Class=%s AND IID=%s""",(itemclass,iid))
			x = cur.fetchall()
			ms.close()
			
			print "Content-Type: text/html\n\n"
			print "<HTML>\n<HEAD>"
			print "<META NAME=\"ROBOTS\" CONTENT=\"NOINDEX, NOFOLLOW, NOSNIPPET\">"
			print "\t<TITLE>1</TITLE>\n"
			print "</HEAD>\n<BODY>"
			if str(x[0][0]) == "S" or str(x[0][0])=="Set([\'S\'])":
				print "<h1>Service Information Has Been Modified:</h1>"
			else:
				print "<h1>Item Information Has Been Modified:</h1>"
			print "<FORM METHOD = post ACTION = \"/cgi-bin/barcodegen.cgi\">"
			print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\" bordercolor=\"#FFFFFF\" width=\"484\">"
			print "\t<tr>"
			print "\t\t<td width=\"389\" colspan=\"2\" bgcolor=\"#808080\">"
			if str(x[0][0]) == "S" or str(x[0][0])=="Set([\'S\'])":
				print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Service Information:</b></font></td>"
			else:
				print "\t\t<font color=\"#FFFFFF\"><b>&nbsp;Item Information:</b></font></td>"
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;" 
			print "\t\tItem Identificaiton Number:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print "\t\t%s</td>"%(form.getvalue("skew"))
			
			print "<input type=\"hidden\" name=\"skew\" value=\"%s\">"%(form.getvalue("skew"))
			print "<input type=\"hidden\" name=\"type\" value=\"B\">"			
			
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tDescription:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			print  "\t\t<textarea name=\"desc\" cols=30 rows =1>%s</textarea></td>"%(x[0][2])
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tOwner:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if x[0][3] =="":
				print "\t\t<textarea name=\"owner\" cols=30 rows =1>%s</textarea></td>"%("(none provided)")
			else:
				print  "\t\t<textarea name=\"owner\" cols=30 rows =1>%s</textarea></td>"%(x[0][3])
			print "\t</tr>\n\t<tr>"
			print "\t\t<td width=\"266\" bgcolor=\"#CCCCCC\"><font face=\"Verdana\" size=\"2\">&nbsp;&nbsp;"
			print "\t\tStatus:</td>"
			print "\t\t<td width=\"215\" bgcolor=\"#CCCCCC\">"
			if str(x[0][4]) == "Set([\'Active\'])":
				print "\t\tActive</td>"
			elif str(x[0][4]) == "Set([\'Inactive\'])":
				print "\t\tInactive</td>"
			elif str(x[0][4]) == "Set([\'Expired\'])":
				print "\t\tExpired</td>"
			else:
				print "\t\t%s</td>"%(str(x[0][4]))
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
	print "\t<TITLE> IID not found!</TITLE>\n"
	print "</HEAD>\n<BODY>"  
	print "<h1>Error: Item Not Found!</h1>"
	print "Sorry, but the Item ID is invalid."
	print "</BODY>\n</HTML>"

if form.getvalue("selection") == "initial":
	lookup()
elif form.getvalue("selection") == "mod":
	modify()
else:
	error()
