#Simple-Fuzzer
'''
This is a simple fuzzer, meant to test what a web server can take before it crashes. This is helpful, as buffer overflows are a common
attack vector for mal-actors.

Please note that this will run until it crashes the web_server (or gets cut-off by the firewall)

If your python is stored elsewhere, you will need to change the path after the Sha-Bang
'''

#!/usr/bin/env python3

import socket
import time 
import sys

ip = 'your_machine_ip' # Please change this to your target
port = 'testing_port' # Please change this to your target port
timeout = 5
prefix = 'Test_Overflow__ ' # Helpful while grepping through logs, 16 characters long
message_content = prefix + "A" * 64

# This is the fuzzer proper. It connects to the target, sends the message, and sees if there is a response 
while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((ip,port))
            sock.recv(1024)
            print("Fuzzing with {} bytes".format(len(message_content))) 
            sock.send(bytes(message_content, "latin-1"))
            sock.recv(1024)
   
   #This block runs if the server crashes
    except:
        print("Crashed at {} bytes".format(len(message_content)))
   
        sys.exit(0)
   #if it didn't crash, add more data
    message_content += 64 * "A"
    time.sleep(1)
    
    
