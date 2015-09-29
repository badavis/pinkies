#!/usr/bin/env python
# encoding: utf-8

# @Author: Gogol Bhattacharya
# @Author: Ben Davis

import MySQLdb as mdb
import sys
import json
import time

from DB import connectToDB

# Class to represent a single pinkie purchase order object.
class Pinkie:

    # Creates a pinkie Object, based off of one of the provided parameters.
    def __init__(self, pinkieId=-1,pinkieJSON=None):
        self.initDataStructures();
        if(pinkieId > -1):
            self.fetchDataFromDB(pinkieId);
        elif(pinkieJSON != None):
            self.loadDataFromJSON(pinkieJSON);

    # Inits all the data structures used by the pinkie object.
    def initDataStructures(self):
        self.objects = {}
        self.s_ulogin = ""
        self.s_time = ""
        self.s_date = ""
        self.funds = {}
        self.requestor =""
    	self.extension = ""
    	self.action = ""
    	self.subTotal = ""
    	self.tax = ""
    	self.shipping = ""
    	self.location = ""
    	self.dateRequired = ""
    	self.totalPrice = ""

    	self.justification = ""
    	self.jopText = ""
    	self.equipLoc = ""
    	self.ucrPropNum = ""
    	self.classInstructed = ""
    	self.quote = ""
    	self.compSoft = ""
    	self.lab = ""
    	self.chemical = ""
    	self.fundSplit = ""
    	self.priority = ""
        self.pid = -1;

        # Vendor Info
    	self.vendor = ""
    	self.name = ""
    	self.address = ""
    	self.city = ""
    	self.state = ""
    	self.postalCode = ""
    	self.POC = ""
    	self.phoneNum = ""
    	self.country = ""
    	self.internet = ""
    	self.faxNum = ""
    	self.ucrAccount = ""

        return;

    # Loads all values for fields based on the pinkies.
    def fetchDataFromDB(self, pinkieId):
        self.pid = pinkieId;

        con = connectToDB();
        cur = con.cursor(mdb.cursors.DictCursor);

        # Gather the SubmittedBy information.
        cur.execute("SELECT * FROM SubmittedBy WHERE PID = %s", (pinkieId));
        resp = cur.fetchone();

        self.s_ulogin = resp["UserID"];
        self.s_date = resp["Date"];
        self.s_time = resp["Time"];
        self.priority = resp["Priority"];
        self.action = resp["Action"];
        self.totalPrice = resp["Total"];

        # Gather the object information
        cur.execute("SELECT * FROM Objects WHERE PID=%s", (pinkieId))
        objects = cur.fetchall();

        i = 0;
        for obj in objects:
            self.objects[i][0] = obj["OID"];
            self.objects[i][1] = obj["Name"];
            self.objects[i][2] = obj["Price"];
            self.objects[i][3] = obj["Quantity"];
            i = i + 1;

        # Gather the fund information
        cur.execute("SELECT * FROM Funds WHERE PID=%s", (pinkieId))
        funds = cur.fetchall();

        i = 0;
        for fund in funds:
            self.funds[i][0] = fund["FundID"];
            self.funds[i][1] = fund["Amount"];
            self.funds[i][2] = fund["FID"];
            i = i + 1;


        # Gather all the extra information
        cur.execute("SELECT * FROM PinkieExtraInfo WHERE PID=%s", (pinkieId));
        resp = cur.fetchone();

        self.dateRequired = resp["DateRequired"];
        self.computer = resp["Computer"];
        self.chemical = resp["Chemical"];
        self.justification = resp["Justification"];
        self.jopText = resp["JustificationText"];
        self.classInstructed = resp["ClassesInstructed"];
        self.equipLoc = resp["EquipmentLocation"];
        self.ucrPropNum = resp["UCRPropertyNumber"];
        self.referenceNumber = resp["ReferenceNumber"];
        self.location = resp["DeliveryLocation"];
        self.quote = resp["Quote"];


        self.vendor = resp["VID"];
        # Gather all the vendor information.
        cur.execute("SELECT * FROM ListOfVendors WHERE VID=%s", (self.vendor));
        resp = cur.fetchone();

    	self.name = resp["VendorName"];
    	self.address = resp["Address"];
    	self.city = resp["City"];
    	self.state = resp["State"];
    	self.postalCode = resp["ZIP"];
    	self.POC = resp["POC"];
    	self.phoneNum = resp["Phone"];
    	self.country = resp["Country"];
    	self.internet = resp["Website"];
    	self.faxNum = resp["Fax"];
    	self.ucrAccount = resp["ucrAccount"];

        con.close();
        return;


    # Fills the pinkies object with data in the JSON object.
    def loadDataFromJSON(self, pinkieJSON):
        for x in xrange(0,len(pinkieJSON["objects"])):
            self.objects[x] = pinkieJSON["objects"][x]


        for x in xrange(0, len(pinkieJSON["funds"])):
            self.funds[x] = pinkieJSON["funds"][x]

        self.s_ulogin = pinkieJSON['requestor']
        self.s_time = pinkieJSON['time'];
        self.s_date = pinkieJSON['date'];
        self.requestor = pinkieJSON['requestor'];
    	self.extension = pinkieJSON['extension'];
    	self.action = pinkieJSON['action'];
    	self.subTotal = pinkieJSON['subTotal'];
    	self.tax = pinkieJSON['tax'];
    	self.shipping = pinkieJSON['shipping'];
    	self.location = pinkieJSON['location'];
    	self.dateRequired = pinkieJSON['dateRequired'];
    	self.totalPrice = pinkieJSON['totalPrice'];
    	self.vendor = pinkieJSON['vendor'];
    	self.name = pinkieJSON['name'];
    	self.address = pinkieJSON['address'];
    	self.city = pinkieJSON['city'];
    	self.state = pinkieJSON['state'];
    	self.postalCode = pinkieJSON['postalCode'];
    	self.POC = pinkieJSON['POC'];
    	self.phoneNum = pinkieJSON['phoneNum'];
    	self.country = pinkieJSON['country'];
    	self.internet = pinkieJSON['internet'];
    	self.faxNum = pinkieJSON['faxNum'];
    	self.ucrAccount = pinkieJSON['ucrAccount'];
    	self.justification = pinkieJSON['justification'];
    	self.jopText = pinkieJSON['jopText'];
    	self.equipLoc = pinkieJSON['equipLoc'];
    	self.ucrPropNum = pinkieJSON['ucrPropNum'];
    	self.classInstructed = pinkieJSON['classInstructed'];
    	self.quote = pinkieJSON['quote'];
    	self.compSoft = pinkieJSON['compSoft'];
    	self.lab = pinkieJSON['lab'];
    	self.chemical = pinkieJSON['chemical'];
    	self.fundSplit = pinkieJSON['fundSplit'];
    	self.priority = pinkieJSON['priority'];

        return;

    # Converts a pinkie to a JSON string.
    def toJSON(self):
        return;

    # Takes the pinkies object and adds it to the database. This object will not
    # have a PID, so I need to get that as soon as i insert it in to the table.
    def toDatabase(self):
        con = connectToDB();
        cur = con.cursor();

        try:
            # We added it to the table.
            cur.execute("INSERT INTO SubmittedBy (UserID,Date,Time) VALUES (%s,%s,%s)" , (self.s_ulogin, self.s_date, self.s_time));

            # Now we need to get the pinkieID.
            cur.execute("SELECT * FROM SubmittedBy WHERE UserID = %s AND Date=%s AND Time=%s", (self.s_ulogin, self.s_date, self.s_time));
            self.pid = int(cur.fetchone()[0]);
            if(self.pid < 0):
                raise ValueError('Could not get a PID!');
        except mdb.Error, e:
            print "ERROR!";
            print "MySQL Error[%d]: %s" % (e.args[0], e.args[1]);
            return self.pid;

        # Now we need to add all the objects with that PID to the database.
        for i in range(len(self.objects)):
            cur.execute("INSERT into Objects (PID,Name,Price,Quantity) VALUES (%s,%s,%s,%s)", (self.pid, self.objects[i][1], self.objects[i][2], self.objects[i][3]));

        # Now we need to add in all the Funds with that PID to the database.
        for f in range(len(self.funds)):
            cur.execute("INSERT into Funds (PID,FundID,Amount) VALUES (%s,%s,%s)", (self.pid, self.funds[f][0], self.funds[f][1]));

        # Now we need to add the extra pinkie information
        cur.execute("INSERT into PinkieExtraInfo (PID,DateRequired,DeliveryLocation,VID, \
                    ReferenceNumber,Computer,Instructional,Chemical,Justification, \
                    JustificationText,EquipmentLocation,UCRPropertyNumber,ClassesInstructed,Quote,Comment) \
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.pid, self.dateRequired, self.location, 1, "PLACEHOLDER",
                                                                                self.compSoft, self.lab, self.chemical, self.justification,
                                                                                self.jopText, self.equipLoc, self.ucrPropNum,
                                                                                self.classInstructed, self.quote, "PLACEHOLDER")) #replace placeholder with actual values later

        # Commit all these changes to the database.
        con.commit();
        con.close();
        return self.pid;
