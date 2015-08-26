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

    # Inits all the data structures used by the pinkie object.
    def initDataStructures(self):
        self.objects = [][][][];
        self.s_ulogin = "";
        self.s_time = "";
        self.s_date = "";
        self.funds = [][][];
        self.pid = -1;

    # Loads all values for fields based on the pinkies.
    def fetchDataFromDB(self, pinkieId):
        self.pid = pinkieId;

        con = connectToDB();
        cur = con.cursor(mdb.cursors.DictCursor);

        # Gather the SubmittedBy information.
        cur.execute("SELECT * FROM SubmittedBy WHERE PID = %i", pinkieId);
        resp = cur.fetchone();

        self.s_ulogin = resp["UserID"];
        self.s_date = resp["Date"];
        self.s_time = resp["Time"];

        # Gather the object information
        cur.execute("SELECT * FROM Objects WHERE PID=%i", pinkieId)
        objects = cur.fetchall();

        i = 0;
        for obj in objects:
            self.objects[i] = obj["OID"];
            self.objects[i][i] = obj["Name"];
            self.objects[i][i][i] = obj["Price"];
            self.objects[i][i][i][i] = obj["Quantity"];
            i = i + 1;

        # Gather the fund information
        cur.execute("SELECT * FROM FUNDS WHERE PID=%i", pinkieId)
        funds = cur.fetchall();

        i = 0;
        for fund in funds:
            self.funds[i] = fund["FID"];
            self.funds[i][i] = fund["FundID"];
            self.funds[i][i][i] = fund["Amount"];
            i = i + 1;


    # fills the pinkies object with data in the JSON object.
    def loadDataFromJSON(self, pinkieJSON):
        json.loads(pinkieJSON);


    # Converts a pinkie to a JSON string.
    def toJSON(self):

   # Takes the pinkies object and adds it to the database.
   def toDatabase(self):
