Name: Evan Vetter Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Evan Vetter

Week 3 Writeup

Part 1: Eric Norman is listed as a Controls Specialist on the website, and implies in his social media (reddit, instagram) that he lives in Texas. This can be used to try and build a rapport with him over the phone, if I were to introduce myself as a fellow texan or controls specialist. If I was able to get his phone number or email, I could present myself as a surveyer from the Texas Workforce Commission, looking for data on his occupation. I'm not sure if this front would be able to elicit information about his mother, but I could use it to expand my knowledge of her then contact her directly after finding out enough about her to find her through OSINT.
("Where did you go to college? Where did your parents go to college? What are your parents' names?" I looked up control specialists and they typically have a 4-year degree at a minimum.) 

To dodge suspicion from Eric, I'd prepare appropriate webpages from https://twc.texas.gov/ to show him that my program is a thing that exists, and prepare illegitimate email addresses/phone numbers if he asked me about my supervisor. 

When talking to his mother, I'd masquerade as a census official, especially since the 2020 census is coming up soon. The questions about pet name, ATM id, and web browser would sound fishy coming from a census official, so I'd have to save them for later on my call with her and space them out. If she questioned me about the questions individually, I'd say that the census bureau was partnering with the Fish and Wildlife Service, Federal Reserve, and Federal Communications Commission for each question respectively. Those questions mostly fall under the purview of each of the corresponding departments.

Part 2:
 Wattsamp.net had exposed ports 20, 80, and 1337. Closing 1337 at the minimum would be the first step, since it was able to be exploited as proven by the week two assignment. 

Eric should install a password generation/repository program like Keepass or Lastpass to create unique passwords both for his account on his website as well as his other accounts. His password for wattsamp.net being on rockyou.txt implies that his other accounts have similarly-weak passwords in use.

 His webserver is running apache 2.4.29 as well, which has many known security vulnerabilities (https://www.cvedetails.com/vulnerability-list.php?vendor_id=45&product_id=66&version_id=241078&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=3&trc=15&sha=e3f39e55231940b8282f47396e556881d5954cd3 ) which includes code execution vulnerabilities. I would recommend to him an upgrade to the current version, 3.1, to avoid DOS or XSS attacks.