#!/usr/bin/env python
# encoding: utf-8

# called by a php script to add the file to the server.
import sys

import pinkie

try:
    pinkie = new Pinkie(pinkieJSON=sys.argv[1]);
    pinkie.toDatabase();
    print "Success!";
except:
    print "[!]ERROR[!]";
    sys.exit(1);
