# Writeup 8 - Binaries II

Name: *Evan Vetter*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Evan Vetter*

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

The password is generated using a random generator seeded based on the system clock. This is vulnerable, since it can be reproduced by generating a duplicate password concurrently to server.c. 

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

Line 68 uses gets to process the execute command function, which is vulnerable to buffer overflow exploits. Using fgets instead is an easy fix.
Having the password generated clientside (line 90) is also vulnerable, since even if I couldn't see the code, it would be visible on the stack. Using authenticators instead is a common practice in SCIFs, as a two-part system concatenating static passwords and personal authenticator strings, since an attacker would need to know the authenticator seed for a given password as well as the password.

3. What is the flag?
CMSC389R-{expl017-2-w1n}

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

I ran "./rando & nc ec2-18-222-89-163.us-east-2.compute.amazonaws.com 1337" in order to print out a duped password at the same time as I connected to the server. rando.c is just a copy paste of the password generation code in server.c, and is included in the writeup folder. After getting admin privileges, the exec_command function uses gets to process user input, which is vulnerable. The user input variable "buff" is adjacent to the char[] of valid commands on the stack. The user input has a size of 32, putting it 32 bytes away from the commands array on the stack. I input "cat flag" followed by 25 spaces, twice. Since "cat flag" is 8 characters long, another 25 spaces would put me into the root of the command array, since 25+8=33. Using spaces was relevant since the bash parser ignores them but they still operate as a nop sled for the stack. This put me in the commands array, where the second copy of the string caused it to be entered into the valid commands list. The function then compared my input to itself, then ran it. After verifying that my cat flag string was the same as the one it had, it ran cat flag against its own environment.
