#!/usr/bin/env python3

# Import appropriate shell utilities and OS dependent functions
import shutil
import os

def main():

    # Start script at /home/student/mycode
    os.chdir("/home/student/mycode")

    # Copy file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # Copy directory or create directory if it does not exist
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
