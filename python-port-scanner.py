# This is a simple Python Port Scanner. This was a way to start learning how to use python's socket module
# It is meant to be executable from the terminal

#this portion is all about dealing with the command line. You must give the agrs after executing the file

import sys
import getopt
import socket


# This function checks all agrs given, and can display a help message when needed
def opt_parser(argv):
    arg_ip = ""
    arg_start_port = ""
    arg_end_port = ""
    arg_help = "{0} -i <ip_addr> -s <start_port> -e <end_port>".format(argv[0])
    
    #This try sets all the arguments given, and returns a help message if there is a error in a given argument
  try:
        opts, args = getopt.getopt(argv[1:], "h:i:s:e:", ["help", "ip_addr=", "start_port=", "end_port="])
      except:
        print(arg_help)
        sys.exit(2)
    
  #This now sets the variables to match the given arguments, or displays the help message if asked for    
        for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--ip_addr"):
            arg_ip = arg
        elif opt in ("-s", "--start_port"):
            arg_start_port = arg
        elif opt in ("-e", "--end_port"):
            arg_end_port = arg

  # We now call this function to parse the given arguments 
if __name__ == "__main__":
    opt_parser(sys.argv)

# This ensures that the end port is greater than the start port. If it isn't, an error message will be written
if arg_end_port < arg_start_point:
  port_error= ("End port less than start point. Please ensure that the end port is greater than the start point".format(argv[0])
  print(port_error)
               
# Here is the port scanner proper. To make it obvious, a list will be printed in terminal displaying all open ports              
for port in range(int(arg_start_point),int(arg_end_port)):
  try:
    s = socket.socket(socket.AF_INET, sk.SOCK_STREAM)
    s.settimeout(1000)
    s.connect((arg_ip,port))
    print("OPEN PORT: {}".format(port))
    s.close
  except: continue
    
