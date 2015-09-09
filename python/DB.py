#!/usr/bin/env python
# encoding: utf-8

# Used to hold all the data required to connect to the database.
# @Author Gogol Bhattacharya

import MySQLdb as mdb
import unitTestHelper as uth

# Connect to the MySQL DB
def connectToDB():
    host = "localhost";
    user = "pinkies";
    db = "pinkies2";
    pw = "pinkies2";
    conn = mdb.connect(host, user, pw, db);
    return conn;

# Set up test values.
def setUpTestValues():
    uth.printInfo("[SETUP] Connecting to Database...");
    con = connectToDB();
    cur = con.cursor();
    uth.printSuccess("[SETUP] Success!");

    # Add to the SubmittedBy table.
    try:
        uth.printInfo("[SETUP] Adding test values to SubmittedBy table...");
        cur.execute("INSERT INTO SubmittedBy (UserID,Date,Time) VALUES (%s,%s,%s)" , ("PinkieTest", "TEST-DATE", "TEST-TIME"));
        uth.printSuccess("[SETUP] Success!");
    except:
        uth.printFailed("[SETUP] Failed to add test values to SubmittedBy table...");
        raise Exception();

    try:
        uth.printInfo("[SETUP] Fetching PID from SubmittedBy table...");
        cur.execute("SELECT * FROM SubmittedBy WHERE UserID = %s AND Date=%s AND Time=%s", ("PinkieTest", "TEST-DATE", "TEST-TIME"));
        pid = int(cur.fetchone()[0]);
        if(pid < 0):
            raise ValueError('Could not get a PID!');

        uth.printSuccess("[SETUP] Success!");
    except:
        uth.printFailed("[SETUP] Failed to fetch PID from SubmittedBy table...");
        raise Exception();

    # Add to the Objects table.
    try:
        uth.printInfo("[SETUP] Adding Test object to the Objects table...");
        cur.execute("INSERT into Objects (PID,Name,Price,Quantity) VALUES (%s,%s,%s,%s)", (pid, "TEST-OBJECT", "1.00", "1"));
        uth.printSuccess("[SETUP] Success!");
    except:
        uth.printFailed("[SETUP] Failed to add Test objects to the Objects table...");
        raise Exception();

    # Add to the Funds table.
    try:
        uth.printInfo("[SETUP] Adding Test fund to the Funds table...");
        cur.execute("INSERT into Funds (PID,FundID,Amount) VALUES (%s,%s,%s)", (pid, "TEST-FUND", "1"));
        uth.printSuccess("[SETUP] Success!");
    except:
        uth.printFailed("[SETUP] Failed to add Test fund to the Funds table...");
        raise Exception();

    # Add to the UploadedFiles table.
    try:
        uth.printInfo("[SETUP] Adding Test file to the UploadedFiles table...");
        cur.execute("INSERT into UploadedFiles (PID,Path,Name) VALUES (%s,%s,%s)", (pid, "TEST-FILE-PATH", "TEST-FILENAME"));
        uth.printSuccess("[SETUP] Success!");
    except:
        uth.printFailed("[SETUP] Failed to add Test file to the UploadedFiles table...");
        raise Exception();

    # Commit our changes to the database.
    con.commit();
    uth.printSuccess("[SETUP] All values added successfully. Changes have been committed");
    # Return the PID for easy removal.
    con.close();
    return pid;

def removeTestValues(pidToRemove):
    uth.printInfo("[CLEANUP] Connecting to Database...");
    con = connectToDB();
    cur = con.cursor();
    uth.printSuccess("[CLEANUP] Success!");

    try:
        uth.printInfo("[CLEANUP] Removing from SubmittedBy...")
        cur.execute("DELETE FROM SubmittedBy WHERE PID = %s" , (pidToRemove));
        uth.printSuccess("[CLEANUP] Success!");
    except:
        uth.printFailed("[CLEANUP] Failed to remove from SubmittedBy...");
        raise Exception();

    # Commit the changes and close the connection.
    con.commit();
    uth.printSuccess("[CLEANUP] All values removed successfully. Changes have been committed.");
    con.close();
    return;
