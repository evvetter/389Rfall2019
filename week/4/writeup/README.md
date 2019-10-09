# Writeup 2 - Pentesting

Name: *Evan Vetter*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Evan Vetter*

## Assignment Writeup

### Part 1 (45 pts)
Command: "5; cat /home/flag.txt"
Flag: CMSC389R-{p1ng_as_a_$erv1c3}
Heads up, there's something going on with the italicization. I imagine it's something to do with backslashes or asterisks.
Thought process: Before using cat to print out the flag.txt, I sent the command "5; ls /*\n" in order to print out the contents of every folder in the system. I found flag.txt by doing that, then fed cat /home/flag.txt into the injection. The idea behind the command injection is just that the service processes the full input, but reads the part after a semicolon as a new command.
Prevention: Sanitizing inputs before processing them is a good idea. One option is to only allow numbers and periods, since that's all an IP pinger should need. If anything else is sent, reject it and don't process it. Running a regex process on it to filter it to only the part of the input should be doable. ex: reg = re.search("([\d\.]*)", input) should work, then use reg.group(0) for the command processor.


### Part 2 (55 pts)

Well, this one is a bit late. I got stuck on this one over the weekend (was sick friday), and came in for office hours on tuesday to find out that i was coming at it from the wrong angle (reverse shell) rather than just repeated command injections with user prompts. The idea is that you store the working directory of the user by using pwd initially to store the location of the user, then updating that variable every time you cd. For other inputs, you append the working directory variable to the input, e.g cat flag.txt would be converted into cat path/flag.txt . I was roughly 2/3 through implementing this when my VM decided to stop working on the network after moving back to my house's wifi, so i'm submitting this as-is with how late it is already. I use regex groups to convert commands into a first and second half, with the first half being the pull/ls/cd/etc, and the second half being the destination. The first half is checked in a switch case (if cd then x else if ls then y ...) with the second half being modified in the s.send call.
