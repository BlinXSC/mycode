#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# import crayon module
import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'Handshaking. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            if mycmds == "shutdown":
                print("Attempting to send command --> ", crayons.red(mycmds))
            else:
                print(f'Attempting to send command --> {crayons.green(mycmds)}')
            # we'll learn to write code that sends cmds to device here
    return None

def devicereboot(devicecmd):

    for ip in devicecmd.keys(): 
        print(f"Connecting to {ip}\n")

    print(f"{crayons.green('REBOOTING NOW!')}\n")

    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.blue('network')} device command pusher") # welcome message

    ## get data set
    print(f"\n{crayons.green('Data set found')}\n") # replace with function call that reads in data from file

    ## run
    devicereboot(devicecmd) # call function to push commands to devices

# call our main function
main()
