"""
If we want to represent a group of Strings according to a particular format/pattern then we
should go for Regular Expressions

Eg 1: We can write a regular expression to represent all mobile numbers
Eg 2: We can write a regular expression to represent all mail ids.

The main important application areas of Regular Expressions are
1.validation login
2.To develop Pattern matching applications (ctrl-f in windows, grep in UNIX etc)
3.To develop Translators like compilers, interpreters etc
4. To develop digital circuits

hum hamari appication ke hisab se regular Expression ko devlope kar sakte hai
"""
# 1. compile()

"""
compile() function to compile a pattern into RegexObject

pattern = re.compile("ab")

Efficiency: The pattern is compiled only once and reused, saving computation time.
Convenience: Allows chaining methods like search, findall, match on the compiled pattern.
Flags: Easier to apply flags when precompiling a pattern.
"""

# 2.finditer()
"""
Returns an Iterator object which yields Match object for every Match

matcher = pattern.finditer("abaababa")

Match object following methods:-
1. start() --> Returns start index of the match
2. end() --> Returns end+1 index of the match
3. group() --> Returns the matched string
"""

    
"""
Pre defined (Character classes)**: page 275:-
\s --> Space character
\S --> Any character except space character
\d --> Any digit from 0 to 9 (only-Digit lega charcter ke siva)
\D --> Any character except digit (charcter lega lekin Digit ko chhod kar)
\w --> Any word character [a-zA-Z0-9] (special symbol consider nahi karega Any)
\W --> Any character except word character (Special Characters)
. --> Any character including special characters


"""    
import re
matcher = re.finditer(r"\D","a7b k@9z") # 
for match in matcher:
    print(match.start(),"......",match.group())


"""
Qunatifiers:
We can use quantifiers to specify the number of occurrences to match.
a --> Exactly one 'a'
a+ --> Atleast one 'a'
a* --> Any number of a's including zero number
a? --> Atmost one 'a' ie either zero number or one number
a{m} --> Exactly m number of a's    Eg:- x=a{3} :- 5....aaa
a{m,n} --> Minimum m number of a's and Maximum n number of a's

Note:
^x --> It will check whether target string starts with x or not
x$ --> It will check whether target string ends with x or not
"""

import re
matcher = re.finditer("a","abaabaaab")
for match in matcher:
    print(match.start(),".....",match.group())



"""
Important functions of re module:
1. match()
2. fullmatch()
3. search()
4.findall()
5.finditer()
6. sub() :- ye replace karta hai jisse karva no ho Eg:- s=re.sub("[a-z]","#","a7b9c5k8z"
7.subn() :- ye same replace karta hai ass sub but isme replace numbers bhi hume milenge kitne numbers replace huve woh bhi..
8. split() :- Eg:- l=re.split(",","sunny,bunny,chinny,vinny,pinny")
9. compile()
"""    

# 1 match():
# import re
# s = input("Enter pattern to check:")
# m = re.match(s,"abcabdefg")
# if m!= None:
#     print("Match is avilable at the beginng of the string")
#     print("Start Index:",m.start(),"and End Index:",m.end()) 
# else:
#     print("Match is not available at the beging of the String")   
"""
case1
Enter pattern to check:abc
Match is avilable at the beginng of the string
Start Index: 0 and End Index: 3

case2
Enter pattern to check:bde
Match is not available at the beging of the String
"""
# 2 full match():

# import re
# s=input("Enter pattern to check: ")
# m=re.fullmatch(s,"ababab")
# if m!= None:
#     print("Full String Matched")
# else:
#     print("Full String not Matched")

"""
Case 1
Enter pattern to check: ab
Full String not Matched

case 2
Enter pattern to check: ababab   True*
Full String Matched
"""    

# 3 search():

# import re
# s=input("Enter pattern to check: ")
# m=re.search(s,"abaaaba")
# if m!= None:
#     print("Match is available")
#     print("First Occurrence of match with start index:",m.start(),"and end index:",m.end())
# else:
#     print("Match is not available")

"""
case 1:-
Match is available          # True**
First Occurrence of match with start index: 2 and end index: 5

case 2:-
Enter pattern to check: bbb  # False **
Match is not available
"""    


# 4. findall()

# import re
# l=re.findall("[0-9]","a7b9c5kz")
# print(l)  # out put :-['7', '9', '5']

# 5. finditer() 

import re
itr=re.finditer("[a-z]","a7b9c5k8z") # ye only a-z lega number's nahi [a-z]
for m in itr:
    print(m.start(),"...",m.end(),"...",m.group())


"""
Returns the iterator yielding a match object for each match.
On each match object we can call start(), end() and group() functions.

out put:-
0 ... 1 ... a
2 ... 3 ... b
4 ... 5 ... c
6 ... 7 ... k
8 ... 9 ... z
"""    

# 6. sub()
# sub means substitution or replacement

import re
s = re.sub("[a-z]","#","a7b9c5k8z")
print(s)  # output :- #7#9#5#8# 

# Note*:- Every alphabet symbol is replaced with # symbol

# 7. subn()

"""
It is exactly same as sub except it can also returns the number of replacements.
This function returns a tuple** where first element is result string and second element is number of
replacements.
(resultstring, number of replacements)
"""

import re
t=re.subn("[a-z]","#","a7b9c5k8z")
print(t)
print("The Result String:",t[0])
print("The number of replacements:",t[1])

# 8. split() :- ye return karega list of tokens.

import re
l=re.split(",","sunny,bunny,chinny,vinny,pinny")
print(l)
for t in l:
   print(t)

# Another Example :- page:- 282

import re
l=re.split("\.","www.sanketsoft.com") # . dot se kardega spilt.. isko
for t in l:
    print(t)   


# ^ symbol:- isse pata chalega given target strings starts with out provided pattern or not...(It Return match object otherwise None  )

import re
s="Learning Python is Very Easy"
res=re.search("^Learn",s) # ^ ye symbol Starting me hi laga na cahiye varna Answer will be wrong
if res != None:
    print("Target String starts with Learn")
else:
    print("Target String Not starts with Learn")

# $ symbol:-  isse pata chalega given target strings Ends with out provided pattern or not... It Return match object otherwise None  

import re
s="Learning Python is Very Easy"
res=re.search("Easy$",s) # $ ye symbol End me hi laga na cahiye varna Answer will be wrong 
if res != None:
   print("Target String ends with Easy")
else:                         
    print("Target String Not ends with Easy")  # out:- Target String ends with Easy


"""
Rules:
1. The allowed characters are a-z,A-Z,0-9,#
2. The first character should be a lower case alphabet symbol from a to k
3. The second character should be a digit divisible by 3
4. The length of identifier should be atleast 2.

[a-k][0369][a-zA-Z0-9#]*
"""    
#---------------#----------------#---------------#------------------#--------
# App2: Write a python program to check whether the given string is Yava
# language identifier or not?

# import re
# s=input("Enter Identifier:") # Enter Identifier:a6KK7z## or invalid:- k7b9 
# m=re.fullmatch("[a-k][0369][a-zA-Z0-9#]*",s)
# if m!= None:
#     print(s,"is valid Yava Identifier")
# else:
#     print(s,"is invalid Yava Identifier") 
#---------------#----------------#---------------#------------------#--------
"""
App3: Write a Regular Expression to represent all 10 digit mobile numbers.
Rules:
1. Every number should contains exactly 10 digits
2. The first digit should be 7 or 8 or 9

[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
or
[7-9][0-9]{9}
or
[7-9]\d{9}
"""
#---------------#----------------#---------------#------------------#--------

# App4: Write a Python Program to check whether the given number
# is valid mobile number or not?

# import re
# n=input("Enter number:")
# m=re.fullmatch("[7-9]\d{9}",n)
# if m!= None:
#     print("Valid Mobile Number")
# else: 
#     print("Invalid Mobile Number")

#-----------#-----------Web Scraping by using Regular Expressions:---------------#------------------#--------

"""
The process of collecting information from web pages is called web scraping. In web scraping to
match our required patterns like:-
*mail ids, mobile numbers we can use regular expressions.

simple :- hum webpages se informations collect karte hai is process ko web scraping kaha jata hai...
jiska use hum mail id ,mobile numbers match karne me use karte hai..
"""
import re,urllib
import urllib.request
sites="google rediff".split()
print(sites)
for s in sites:
    print("Searching...",s)
    u=urllib.request.urlopen("http://"+s+".com")
    text=u.read()
    title=re.findall("<title>.*</title>",str(text),re.I)
    print(title[0])
#---------------#----------------#---------------#------------------#--------
# Eg: Program to get all phone numbers of redbus.in by using web
# scraping and regular expressions

import re,urllib
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=u.read()
numbers=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I)
for n in numbers:
    print(n)
#---------------#----------------#---------------#------------------#--------
# Eg:- check whether the given **mail id is valid gmail id or not?

import re
s=input("Enter Mail id:")
m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if m!=None:
    print("Valid Mail Id")
else:
    print("Invalid Mail id")

"""
Enter Mail id:sanketmajithiya777@gmail.com
Valid Mail Id
"""    
#---------------#----------------#---------------#------------------#--------
# check whether given car registration number is valid Gujarat State
#  Registration number or not?

import re
s=input("Enter Vehicle Registration Number:")
m=re.fullmatch(r"(?i)gj[012][0-9][A-Z]{2}\d{4}",s)
if m!=None:
    print("Valid Vehicle Registration Number") # gj27AB1234  or GJ07EA7777
else:
    print("Invalid Vehicle Registration Number")
#---------------#----------------#---------------#------------------#--------

# check whether the given mobile number is valid OR not
#  (10 digit OR 11 digit OR 12 digit)

import re
s=input("Enter Mobile Number:")
m=re.fullmatch("(0|91)?[7-9][0-9]{9}",s)
if m!=None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")