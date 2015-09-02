#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable()     # for troubleshooting
#import pinkie
import json
import re

print("Content-Type: text/html\n") # HTTP header to say HTML is following
# end of headers

form = cgi.FieldStorage()


print ("<html><body><h1>Test</h1><br><h2>")
#print form
for i in form:
	print (form[i].value)
print ("</h2></body></html>")

qty_temp = form.getlist("qty")
qty_list = ",".join(qty_temp)
print qty_list

tempJSON = {}
for key in form: 
	endsInNum = re.search(r'\d+$',key)

		tempJSON[key] = form[key].value

		

print tempJSON






