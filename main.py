# Created 12/19/2020
# This is a secure password generator using alphabetic and numeric characters
# This generates crptographically secure random passwords using the secrets module
# This also calcuates the probability of randomly guessing the password

# Written by Paul A. Turner from the University of Central Florida
# College of Engineering & Computer Science - Department of Computer Science

import secrets
import string
import math
import os

a = input("Enter Number of Requests: ")
b = input("Enter Password Length: ")
c = int(a)
d = int(b)

# calculates the probability of the password being randomly guessed
# passwords consist of letters, punctuation, and digits, totaling 36 possibilities. choosing the right letter is a 1/68 chance, which exponentially grows as more characters are added to the password.
# formula: (1/36)^n, where n is the number of chacters in the password 
prob = pow((1/36), d)

# Generates a session token, represented in hexidecimal - used for searching for the output file
sessionToken = secrets.token_hex(2)

# prints out the probability of guessing the password randomly; due to low probability, probability is represented as Ne-n, where N is the probability, and -n is the number of decimal places unable to be represented.
print("\n>>> Probability of guessing individual passwords: " + str(prob))

# creates the alphabet of characters that can be chosen for the password
alphabet = string.ascii_letters + string.digits

# Python FILE I/O
out = open("output.txt", 'w')
out.write(">>> Session Token: " + sessionToken +"\n\n")

# Prints the output of the generated passwords
i = 0

while (i < c):
    password = ''.join(secrets.choice(alphabet) for i in range (d))
    if(i == (c-1)):
        out.write(str(i+1) +":\t" + password)
        print(str(i+1)+":\t"+password)
    else:
        out.write(str(i+1) +":\t"+ password+"\n")
        print(str(i+1)+":\t"+password+"\n")
    i = i+1
out.close()
j = 0
ans = ''
print("\n")
# File is closed and provided to the user. For security purposes, the file may then be immediately deleted so a copy does not exist on the system
while(j == 0):
    ans = input("Delete Password file? (y/n): ")
    if (ans == 'y' or ans == 'Y' or ans == 'n' or ans == 'N'):
        j=1
    else:
        print("Error: Invalid Response")

print("\n>>> You session token is: " + sessionToken)

# If answer to deletion is 'y' or 'Y', file is deleted
if (ans == "y" or ans == "Y"):
    os.remove("output.txt")
    print("File deleted")

# hashCode = int(sessionToken, 16)%27 --> translates hexcode into int and then modulo into a hash value
# print(">> File Assigned to Index " + str(hashCode)) --> prints the array index location for the file
# print(format(int(sessionToken, 16), "b")) --> prints session token in binary format

print("Exiting...\n")
