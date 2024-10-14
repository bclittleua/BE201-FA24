#! /usr/bin/env python
import re, sys, os, random
from time import sleep
flag = 0       #pass/fail indicator
ecode = "\n"
error1 = "Too short, minimum of 16 characters.\n"
error2 = "No lower case letters.\n"
error3 = "No upper case letters.\n"
error4 = "No numbers 0-9.\n"
error5 = "Contains spaces, no spaces allowed.\n"
error6 = "No acceptable special characters: !@#$%^&*()_+?.,-=\n"
#
try:
    print("-------PWCHECK--------")
    print("A secure password must contain:\n -at LEAST 16 characters\n -lowercase letters\n -UPPERCASE letters\n -Numbers\n -Special characters: !@#$%^&*()_+-=?,.\n -NO spaces \n")
    ui = raw_input("Enter password to be tested: ") # ui = user input
    password = '"' + ui + '"'                       # password has to be wrapped in quotes to properly read the special characters
    print("ANALYZING: " + ui)                       # wanted to give appearance that script was thinking, makes UX feel better
    sleep(random.randrange(3))
    if (len(password)<16):
        flag = -1
        ecode += str(error1)
    if not re.search("[a-z]", password):
        flag = -1
        ecode += str(error2)
    if not re.search("[A-Z]", password):
        flag = -1
        ecode += str(error3)
    if not re.search("[0-9]", password):
        flag = -1
        ecode += str(error4)
    if re.search("\s", password):
        flag = -1
        ecode +=  str(error5)
    if not re.search("[\!\@\#\$\%\^\&\*\(\)\_\+\-\=\?\,\.]", password):
        flag = -1
        ecode += str(error6)
        #
    if flag ==-1:
        print("\nRESULT: Password FAILED")
        sleep(1)
        print("REASON(s): " + ecode)
        sleep(1)
        print("Please try again or CTRL+C to cancel.\n\n")
        execfile("/usr/local/bin/pwcheck")
    elif flag == 0:
        print("\nRESULT: This password is strong! Well done!")
except KeyboardInterrupt:
    print(" Exiting pwcheck...\n")
    sys.exit(0)
