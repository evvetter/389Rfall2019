# Writeup 2 - OSINT

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)


 Found instagram.com/ejnorman84, profile linked to wattsamp.net. Real name is Eric J Norman.

1.EJNORMAN works at Watts Amp Energy at wattsamp.net.
2.Found their instagram, reddit through namechk.com. 
3.Checked securitytrails.com and domaindossier, searched for wattsamp.net, received IP address 157.230.179.99  
4.Found the hidden file/directory wattsamp.net/assets, /server-status through running dirb on the url.
5. Shodan.io lists the server as being located in NY and hosted by Digital Ocean. Shodan specifically lists port 80 as being open and running off apache 2.4.29. 
6. Running an intensive nmap scan also found port 1337. Port 1337 is the correct  port.
7. Shodan also says that the server is running ubuntu.
8: *CMSC389R-{html_h@x0r_lulz}*
*CMSC389R-{Do_you-N0T_See_this}*
*CMSC389R-{n0_indexing_pls}*
### Part 2 (75 pts)

Wrote a parser to read the captcha, then to compute the expected result. After that, I created an iterator to run through rockyou.txt for each line in the file, printing the current password and success/fail result for each. The "count" value on the iterator was made because of connection issues causing the script to fail, so I could start back up where the connection failed.
PW: hello1
Flag: *CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}*