#!/usr/bin/env python
import html
import cgi
import cgitb; cgitb.enable()     # for troubleshooting

print("Content-Type: text/html") # HTTP header to say HTML is following
print()                          # blank line, end of headers

form = cgi.FieldStorage()
print (form["action"].value)
