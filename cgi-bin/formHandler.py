#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable()     # for troubleshooting
import sys
sys.path.insert(0,'/var/www/html/pinkies/python')
from pinkie import Pinkie
import json
import re

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

	requestor = getInput("requestor",form)
	extension = getInput("extension",form)
	action = getInput("action",form)
	subTotal = getInput("sub-total",form)
	tax = getInput("tax",form)
	shipping = getInput("shipping",form)
	location = getInput("location",form)
	dateRequired = getInput("date-required",form)
	totalPrice = getInput("total-price",form)
	vendor = getInput("vendor", form)
	name = getInput("name",form)
	address = getInput("address",form)
	city = getInput("city",form)
	state = getInput("state",form)
	postalCode = getInput("zip",form)
	POC = getInput("POC",form)
	phoneNum = getInput("phone",form)
	country = getInput("country",form)
	internet = getInput("internet",form)
	faxNum = getInput("fax",form)
	ucrAccount = getInput("account",form)
	justification = getInput("justification",form)
	jopText = getInput("jop-text",form)
	equipLoc = getInput("equip-loc",form)
	ucrPropNum = getInput("ucr-prop-num",form)
	classInstructed = getInput("class",form)
	quote = getInput("quote",form)
	compSoft = getInput("computer",form)
	lab = getInput("lab",form)
	chemical = getInput("chemical",form)
	fundSplit = getInput("funds",form)
	priority = getInput("priority",form)

	JSONPinkie = {}
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
