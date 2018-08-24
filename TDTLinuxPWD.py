#!/usr/bin/python
#Developed by Tiago Neves
#Github: https://github.com/TiagoANeves
#Version: 1.0
#All rights reserved

#Import necessary modules
import crypt
import sys
import os
from argparse import ArgumentParser

os.system("clear")

#Color scheme
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Create Banner
def banner():
    print("""%s
      _____   ____    _____   _       _                          ____   __        __  ____
     |_   _| |  _ \  |_   _| | |     (_)  _ __    _   _  __  __ |  _ \  \ \      / / |  _ \\
       | |   | | | |   | |   | |     | | | '_ \  | | | | \ \/ / | |_) |  \ \ /\ / /  | | | |
       | |   | |_| |   | |   | |___  | | | | | | | |_| |  >  <  |  __/    \ V  V /   | |_| |
       |_|   |____/    |_|   |_____| |_| |_| |_|  \__,_| /_/\_\ |_|        \_/\_/    |____/ %s%s

     # Coded By Tiago Neves
     # Github https://github.com/TiagoANeves

    """ % (bcolors.OKBLUE, bcolors.ENDC, bcolors.FAIL))

# Arguments Parser
parser = ArgumentParser()
parser.add_argument("-s", "--shadow", help="shadow file")
parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="wordist file %s" %bcolors.ENDC)

# Count wordlist password
def countlines(textfile):
	num_lines = len(open(textfile).readlines(  ))
	return num_lines

# Main function
if __name__ == "__main__":
    try:
        banner()
        print "This program will check the users in the shadow file and use a wordlist to try crack the password hashes."
        print "If wordlist not especified, it will use the wordlist.txt by default."
        print bcolors.ENDC
        args = parser.parse_args()
    except:
        sys.exit(0)
    if len(sys.argv) < 3:
        print bcolors.WARNING + "Usage: python "+sys.argv[0]+" -s shadown -w wordlist.txt\n" + bcolors.ENDC
        print bcolors.WARNING + "Use "+sys.argv[0]+" -h or --help to print the help option\n" + bcolors.ENDC
        sys.exit()
    else:
        print bcolors.HEADER + "Starting the program...\n" + bcolors.ENDC
	numlines = countlines(args.wordlist)
	print bcolors.HEADER + "The file %s%s%s has %s%s%s passwords" %(bcolors.OKGREEN,args.wordlist,bcolors.HEADER,bcolors.OKGREEN,numlines,bcolors.HEADER) + bcolors.ENDC	
        try:
            fileshadow = open(args.shadow,'r')
        except:
            print "Error trying to open shadow file"
            sys.exit()
        users = fileshadow.read().split('\n')
        for user in users:
            if '$' in user:
                userline = user.split(":")
                hashes = userline[1].split("$")
                salt = "$"+hashes[1]+"$"+hashes[2]+"$"
                passfound = 0
                print bcolors.WARNING + "\nBruteforcing password for the user %s%s" %(bcolors.OKGREEN,userline[0]) + bcolors.ENDC
                try:
                    filewordlist = open(args.wordlist,'r')
                except:
                    print "Error trying to open wordlist file"
                    sys.exit()
                passwords = filewordlist.read().split('\n')
		pwdcount = 0
                for password in passwords:
		    try:
		    	pwdcount += 1
                    	print bcolors.WARNING + "Trying %s%s%s of %s%s%s passwords" %(bcolors.OKGREEN,pwdcount,bcolors.WARNING,bcolors.OKGREEN,numlines,bcolors.WARNING) + bcolors.ENDC
                    	result = crypt.crypt(password, salt)
                    	if (result == userline[1]):
                        	sys.stdout.write("\r")
                        	sys.stdout.flush()
                        	print bcolors.OKBLUE + bcolors.BOLD + bcolors.UNDERLINE + "Password found: " + bcolors.OKGREEN + password + bcolors.ENDC
                        	passfound = 1
                        	break
                    	else:
                    		sys.stdout.write("\033[F") #Back to previous line
                    		sys.stdout.write("\033[k") #Clear line
                        	sys.stdout.write("\r")
                        	sys.stdout.flush()
		    except KeyboardInterrupt:
			print bcolors.FAIL + "Bruteforcing interrupted by the user..." + bcolors.ENDC
			break
                if (passfound == 0):
                    print bcolors.FAIL + "Could not find the password for the user "+userline[0] + bcolors.ENDC
