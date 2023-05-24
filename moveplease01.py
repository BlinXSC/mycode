#!/usr/bin/env python3

# Library imports
import shutil
import os

def main():
    # Start in home user directory in mycode
    os.chdir('/home/student/mycode/')

    # Move Raynor with Kerrigan
    shutil.move('raynor.obj', 'ceph_storage/')

    # Change Kerrigan's name
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname +'.obj')

# Call main function
main()
