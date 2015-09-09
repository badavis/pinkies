#!/usr/bin/env python
# coding: utf-8


# Unit test assistance fuctions.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Prints [OKAY] followed by the message.
def printSuccess(msg):
    print "[" + bcolors.OKGREEN + bcolors.BOLD + "OKAY" + bcolors.ENDC + "] " + msg;

# Prints [FAIL] followed by the message.
def printFailed(msg):
    print "[" + bcolors.FAIL + bcolors.BOLD + "FAIL" + bcolors.ENDC + "] " + msg;

# Prints [INFO] followed by the message.
def printInfo(msg):
    print "[" + bcolors.OKBLUE + bcolors.BOLD + "INFO" + bcolors.ENDC + "] " + msg;

def printWarning(msg):
    print "[" + bcolors.WARNING + bcolors.BOLD + "WARN" + bcolors.ENDC + "] " + msg;

def printHeader(msg):
    print "[" + bcolors.HEADER + bcolors.BOLD + bcolors.UNDERLINE + "HEADER" + bcolors.ENDC + "] " + bcolors.OKBLUE + bcolors.UNDERLINE + msg + bcolors.ENDC + " [" + bcolors.HEADER + bcolors.BOLD + bcolors.UNDERLINE + "HEADER" + bcolors.ENDC + "]";

# Assets if two things are equal to each other.
def assertEquals(msg, obj1, obj2):
    if obj1 == obj2:
        printSuccess(msg);
    else:
        printFailed(msg);
        printFailed("Was expecting: %s. Recieved: %s" % (obj1, obj2));

# Asserts if two things are not equal to each other.
def assertNotEquals(msg, obj1, obj2):
    if obj1 != obj2:
        printSuccess(msg);
    else:
        printFailed(msg);
        printFailed("Was not expecting: %s. Recieved: %s" % (obj1, obj2));

def testUnitTestSoftware():
    printHeader("Console color print out.");
    printSuccess("This should be successful!");
    printFailed("This should have failed.");
    printWarning("This is a WARNING.");
    printInfo("This is INFO.");

    printHeader("Assert Testing");
    assertEquals("Does 1 = 1", 1, 1);
    assertNotEquals("Does 1 != 2", 1, 2);

    printInfo("These two tests should fail.");
    assertEquals("Does 1 = 2", 1, 2);
    assertNotEquals("Does 2 != 2", 2, 2);
