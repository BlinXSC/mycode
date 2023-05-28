#!/usr/bin/env python3
"""AAlegre | TLG Learning
   Manually create an rc file or use an import file"""

import csv

# Manually create an rc file
def manual_rc():
    """Manually create an rc file"""

    with open("admin.rc", "a") as outFile:
        osAUTH = input("What is the OS_AUTH_URL? ")
        print("export OS_AUTH_URL=" + osAUTH, file=outFile)

        print("export OS_IDENTITY_API_VERSION=3", file=outFile)

        osPROJ = input("What is the OS_PROJECT_NAME? ")
        print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

        osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
        print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

        osUSER = input("What is the OS_USERNAME? ")
        print("export OS_USERNAME=" + osUSER, file=outFile)

        osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
        print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

        osPASS = input("What is the OS_PASSWORD? ")
        print("export OS_PASSWORD=" + osPASS, file=outFile)

# Create rc using an importfile
def auto_rc():
    """Auto-create an rc file"""

    user_list = input("Please provide the file name you wish to use to create the rc file >>> ")

    with open(user_list, "r") as csvfile:

        # loop across our open file line by line
        for row in csv.reader(csvfile):
            # creates file with the user's name to identify it
            filename = f"{row[3]}.rc"

            # open a file via "with". This file will autoclose when the indentations stop
            with open(filename, "w") as rcfile:
                # use the standard library print function to print our data
                # out to the open file open rcfile (open in write mode)
                print("export OS_AUTH_URL=" + row[0], file=rcfile)
                print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
                print("export OS_USERNAME=" + row[3], file=rcfile)
                print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
                print("export OS_PASSWORD=" + row[5], file=rcfile)

                # all of the indentation ends, so all files are auto closed

    # display this to the screen when all of the looping is over
    print("admin.rc files created!")

# runs program, prompts user if they want to create a single rc manually or multiple automatically
def main():
    """Main program"""

    choice = -1

    print("How do you wish to create rc files today?")
    print("1. Manually")
    print("2. Automatically with an input file")

    while choice != 0:
        try:
            choice = int(input("Please select 1 or 2 , or type \"0\" to exit >>> "))
        except:
            print("Wrong input, please try again.")

        if choice == 1:
            manual_rc()
        elif choice == 2:
            auto_rc()

main()