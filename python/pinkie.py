#!/usr/bin/env python
# encoding: utf-8

# @Author: Gogol Bhattacharya
# @Author: Ben Davis

import MySQLdb as mdb
import sys
import json

import DB

# Class to represent a single pinkie purchase order object.
class Pinkie:

    # Loads a pinkie object from the databse with the given pinkie ID.
    def __init__(self, pinkieId):
        initDataStructures();
        fetchDataFromDB(pinkieId);

    # Loads a pinkie object from the given JSON object.
    def __init__(self, pinkieJSON):
        initDataStructures();
        loadDataFromJSON(pinkieJSON);

    # Inits all the data structures used by the pinkie object.
    def initDataStructures(self):
        self.objects = [][4];
        self.s_ulogin = "";
        self.s_time = "";
        self.s_date = "";
        self.funds = [][3];
        self.pid = -1;
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
            self.funds[i][0] = fund["FID"];
            self.funds[i][1] = fund["FundID"];
            self.funds[i][2] = fund["Amount"];
            i = i + 1;

        return;


    # Fills the pinkies object with data in the JSON object.
    def loadDataFromJSON(self, pinkieJSON):
        return;

    # Converts a pinkie to a JSON string.
    def toJSON(self):
        return;

    # Takes the pinkies object and adds it to the database. This object will not
    # have a PID, so I need to get that as soon as i insert it in to the table.
    def toDatabase(self):
        con = connectToDB();
        cur = con.cursor(mdb.cursors.DictCursor);

        # We added it to the table.
        cur.execute("INSERT into SubmittedBy (UserID,Date,Time) VALUES (%s,%s,%s)", (self.s_ulogin, self.s_date, self.s_time));
        # Now we need to get the pinkieID.
        cur.execute("SELECT 1 FROM SubmittedBy WHERE UserID = %s, Date=%s, Time=%s", (self.s_ulogin, self.s_date, self.s_time));
        self.pid = int(cur.fetchone());

        # Now we need to add all the objects with that PID to the database.
        for i in range(len(self.objects())):
            cur.execute("INSERT into Objects (PID,Name,Price,Quantity) VALUES (%s,%s,%s,%s)", (self.pid, self.objects[i][1], self.objects[i][2], self.objects[i][3]));

        # Now we need to add in all the Funds with that PID to the database.
        for f in range(len(self.funds)):
            cur.execute("INSERT into Funds (PID,FundID,Amount) VALUES (%s,%s,%s)", (self.pid, self.funds[f][1], self.funds[f][2]));

        return;
