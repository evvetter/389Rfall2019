# Writeup 9 - Forensics II

Name: *Evan Vetter*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Evan Vetter*


## Assignment details

### Part 1 (45 Pts)
1: IP address hacked: 159.203.113.181
2: Assessment tools used: I'm not sure what tools were used.
3: Hacker's IP: 142.93.136.81
4: Port used: 42361
5: File stolen, type, recognized: findme.jpeg, jpeg,
It's a picture of a beach with some sculpture of a hand whose fingers are sticking out of the ground.
6: File left behind: greetz.fpff
7: Countermeasures to use to prevent future attacks: I'm not sure what attack was performed or vulnerabilities exploited.

Steps: Ran strings and wireshark on netlog.pcap, found some plaintext in the strings run listing source and destination IP. Filtered the wireshark viewer to those connections, then took a look at the conversation with follow -> tcp. Wireshark lists the port used in the requests. Found that the source requested findme.jpeg, and stored greetz.fpff. findme.jpeg and greetz.fpff were transmitted, and I saved both of those. 

### Part 2 (55 Pts)

Written by:fl1nch
Date: 2019/03/27
Section 1: ASCII, "Hey you, keep looking :)"
Section 2: Coordinate tuple, (52.336035, 4.880673)
Section 3: PNG, image of a terp pointing up with a flag on the side.
Section 4: ASCII, }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
Section 5: ASCII, Some garbage text that I think I messed up parsing.

Flags: CMSC389R-{h0pefully_y0u_didn't_grep_CMSC389R}
CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}

Steps: After finding the author/date in the first 12? bytes, the section count lists the number of chunks to parse. Each one starts with a given hex value, so I made an if/else list to handle each type. For the ascii/utf, I just ran decode on the bytes designated by slen. For the words/dwords/doubles, I read 8/16/16 bytes until I ran out of capacity, printing each. For the coordinates, struct.unpack got both at once. For the images, I created a new file with file.open, and wrote the magic bytes listed for each given type before writing sval to the new file.