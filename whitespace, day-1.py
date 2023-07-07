import string 
print ("hello")
result=string.whitespace
print(result)
print("Aratrika, Ronit")

import string
sentence=("how are you")
for i in sentence:
    if i in string.whitespace:
        print("Printable value is: "+i)

#creating a string with single, double and triple
string1='I am a good boy'
print("String with the use of single quotes: ")
print(string1)
string1="RCB is love"
print("\nstring with the use of double quotes: ")
print(string1)
string1="""KKR is emotion"""
print("\nstring with the use of triple quotes: ")
print(string1)
string1="""Aratrika
Ronit
Subhadip"""
print("Encreating a multi-line string: ")
print(string1)