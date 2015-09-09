#!/usr/bin/env python
# encoding: utf-8

import MySQLdb as mdb
import sys
import unitTestHelper
import DB


def runTests():
    testConnection();
    testTables();

# Used to to basic testing of the mysql database.
def testConnection():
    unitTestHelper.printHeader("Testing connection to database");
    unitTestHelper.printInfo("Attempting to connect to connect to database...");
    try:
        con = DB.connectToDB();

        cur = con.cursor();
        cur.execute("SELECT VERSION()");

        ver = cur.fetchone();

        unitTestHelper.printSuccess("Was able to connect to database! Databse Version: %s" % ver);
        con.close();

    except mdb.Error, e:
        unitTestHelper.printFailed("Error %d: %s" % (e.args[0], e.args[1]));
        sys.exit(1);

def testTables():
    unitTestHelper.printHeader("Testing integrity of tables");
    # Set up for testing.
    unitTestHelper.printInfo("Adding in test values.");
    pidTemp = -1;
    try:
        pidTemp = DB.setUpTestValues();
    except:
        unitTestHelper.printFailed("Failed to set up test values.... Attempting cleanup");
        try:
            DB.removeTestValues(pidTemp);
        except:
            unitTestHelper.printFailed("Failed to clean up test values. Clean up values with PID: %s" % (pidTemp));
        return;


    # Conduct testing...

    # Check the SubmittedBy Table.

    # Check the Objects Table.

    # Check the Funds Table.

    # Check the UploadedFiles Table.

    # Clean up after testing.
    try:
        DB.removeTestValues(pidTemp);
    except:
        unitTestHelper.printFailed("Failed to clean up test values.");
        return;
