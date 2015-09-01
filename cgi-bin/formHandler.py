#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable()     # for troubleshooting

print("Content-Type: text/html\n") # HTTP header to say HTML is following
# end of headers

form = cgi.FieldStorage()

print ("<html><body><h1>Test</h1><br><h2>")
print (form["action"].value)
print ("</h2></body></html>")
