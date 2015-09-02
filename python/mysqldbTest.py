#!/usr/bin/env python
# encoding: utf-8

import MySQLdb as mdb
import sys
import unitTestHelper


# Used to to basic testing of the mysql database.
def testConnection():
    unitTestHelper.printInfo("Attempting to connect to connect to database...");
    try:
        con = mdb.connect('localhost', 'pinkies', 'pinkies2', 'pinkies2');

        cur = con.cursor();
        cur.execute("SELECT VERSION()");

        ver = cur.fetchone();

        unitTestHelper.printSuccess("Was able to connect to database! Databse Version: %s" % ver);
        con.close();

    except mdb.Error, e:
        unitTestHelper.printFailed("Error %d: %s" % (e.args[0], e.args[1]));
        sys.exit(1);
