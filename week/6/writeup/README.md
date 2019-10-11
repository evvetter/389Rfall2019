# Writeup 6 - Binaries I



Name: *Evan Vetter*

Section: *0101*



I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.



Digital acknowledgement: *Evan Vetter*



## Assignment Writeup



### Part 1 (50 pts)



CMSC389R-{di5a55_0r_d13}



### Part 2 (50 pts)

Crackme's 'main' call operated by checking the parameters of the first command it was passed with, then checked an environment variable, then the contents of a nearby file.

The 0'th check made sure that there was any parameter included when main was called.

The first check, check1, compared structural equality of the parameter with another string on the stack, "Oh God". 

Then, it checked for an environment variable bound to FOOBAR of length 8. Check2 compared foobar to data_2016, "seye ym ". This was read backwards into " my eyes". Then, it attempted to open a local file named sesame. If it was successful, then it read at least ten characters from the file, checking each character for equality by converting char to hexadecimal. Converting it backwards into characters, it was reading for "they burn ".



env FOOBAR=" my eyes" ./crackme "Oh God"