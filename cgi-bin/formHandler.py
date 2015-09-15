#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable()     # for troubleshooting
import sys
sys.path.insert(0,'/var/www/html/pinkies/python')
from pinkie import Pinkie
import json
import re
import time

#retrieves the text from an input-text field submitted by the form.
#if key is not in the form, return "none"
def getInput(key,form):
	try:
		value = form[key].value
		return value
	except KeyError:
		return "none"

#creates a list from input-text fields with the same value
def formatList(key,form):
	try:
		temp = form.getlist(key)
		#formatted = ",".join(temp)
		return temp
	except KeyError:
		return "none"

def createObjects():

	qtyL = formatList("qty",form)		# quantity of each object purchased
	stkL = formatList("stock",form)		# stock number of each object purchased
	descL = formatList("desc",form)		# description of each object purchased
	prcL = formatList("price",form)		# price of each object purchased
	totL = formatList("total",form)		# price x quantity of each object purchased (total cost of object)

	objects = {}

	# associates a quantity, stock number,
	# description, price, and total cost for each object
	for x in xrange(0,len(totL)):
		objects[x] = []
		objects[x].append(qtyL[x])
		objects[x].append(stkL[x])
		objects[x].append(descL[x])
		objects[x].append(prcL[x])
		objects[x].append(totL[x])
	return objects


def createFunds():

	fundNames = formatList("fname", form)	# gets list of all funds selected
	amntL = formatList("amount[]",form)		# gets amount input for each fund

	funds = {}
	# for loop to associate an amount with each fund
	for x in xrange(0,len(amntL)):
		funds[x] = []
		funds[x].append(fundNames[x])
		funds[x].append(amntL[x])
	return funds




if __name__ == '__main__':
	print("Content-Type: text/html\n") # HTTP header to say HTML is following
	# end of headers

	form = cgi.FieldStorage()	#variable for the POSTed html-form data
	print ("<html><body><h1>Test</h1><br><h2>")	#html for testing
	#for each in form:
		#print form[each].value #testing
	print ("</h2></body></html>")

	objects = createObjects()
	funds = createFunds()
	JSONPinkie = {}

	JSONPinkie['requestor'] = getInput("requestor",form)
	JSONPinkie['extension'] = getInput("extension",form)
	JSONPinkie['action'] = getInput("action",form)
	JSONPinkie['subTotal'] = getInput("sub-total",form)
	JSONPinkie['tax'] = getInput("tax",form)
	JSONPinkie['shipping'] = getInput("shipping",form)
	JSONPinkie['location'] = getInput("location",form)
	JSONPinkie['dateRequired'] = getInput("date-required",form)
	JSONPinkie['totalPrice'] = getInput("total-price",form)
	JSONPinkie['vendor'] = getInput("vendor", form)
	JSONPinkie['name'] = getInput("name",form)
	JSONPinkie['address'] = getInput("address",form)
	JSONPinkie['city'] = getInput("city",form)
	JSONPinkie['state'] = getInput("state",form)
	JSONPinkie['postalCode'] = getInput("zip",form)
	JSONPinkie['POC'] = getInput("POC",form)
	JSONPinkie['phoneNum'] = getInput("phone",form)
	JSONPinkie['country'] = getInput("country",form)
	JSONPinkie['internet'] = getInput("internet",form)
	JSONPinkie['faxNum'] = getInput("fax",form)
	JSONPinkie['ucrAccount'] = getInput("account",form)
	JSONPinkie['justification'] = getInput("justification",form)
	JSONPinkie['jopText'] = getInput("jop-text",form)
	JSONPinkie['equipLoc'] = getInput("equip-loc",form)
	JSONPinkie['ucrPropNum'] = getInput("ucr-prop-num",form)
	JSONPinkie['classInstructed'] = getInput("class",form)
	JSONPinkie['quote'] = getInput("quote",form)
	JSONPinkie['compSoft'] = getInput("computer",form)
	JSONPinkie['lab'] = getInput("lab",form)
	JSONPinkie['chemical'] = getInput("chemical",form)
	JSONPinkie['fundSplit'] = getInput("funds",form)
	JSONPinkie['priority'] = getInput("priority",form)
	JSONPinkie['time'] = time.strftime("%H:%M:%S");
	JSONPinkie['date'] = time.strftime("%m-%d-%Y");


	JSONPinkie["objects"] = objects
	JSONPinkie["funds"] = funds

	pinkieObj = Pinkie(-1, JSONPinkie)
	pinkieObj.toDatabase()








	#print qtyList
	#print stockList
	#print '<br>'
	#print descList
	#print '<br>'
	#print priceList
	#print totalList
