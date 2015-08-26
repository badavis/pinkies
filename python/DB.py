#!/usr/bin/env python
# encoding: utf-8

# Used to hold all the data required to connect to the database.
# @Author Gogol Bhattacharya

import MySQLdb as mdb

def connectToDB():
    host = "localhost";
    user = "pinkies";
    db = "pinkies2";
    pw = "pinkies2";
    conn = mdb.connect(host, user, pw, db);
    return conn;
