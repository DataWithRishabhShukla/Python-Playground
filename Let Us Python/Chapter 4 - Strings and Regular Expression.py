from common.common_library import clear_terminal

# clear_terminal()

# Escape characters in the 
"""
If there are characters ' " \ in the string it can be retained in the two ways.
    - using the escape character \ 
    - defining using the r" "  , raw string 

"""
s1 = 'test string\'s value'
print(s1)
s2 = r"this is\ raw 'strin' "
print(s2)
s3 = "this is 3rd \\raw string"
print(s3)


"""
String Properties :

Strings are immutable 
Strings can be concatenating using the + 
Strings can be replicated using  * operator 
Weather one string is part of another string can be chekced using in operator 

"""


s = "hello"
#s[0] = 'H' # this will result in the error 
s = "rishabh" # this will work as s is variable it can be reassignes

print('test '* 10)

print('e' in 'hello')
print('z' in 'hello')


"""
Builtin Functions
len()
type()
id()
min()
max()

when we create a string a nameless object of str is created and 
address of this is assigned to the variable 

Just like other 
In Python, you’re right: some functions are used like func(str), while others are used like str.func(). 
The difference comes down to where the function is defined and what kind of object it’s working on.

str.func() — Methods of the string object
These are methods defined specifically for string objects. They operate on the string instance.

These are functions, not tied to the string object itself. 
They’re either built-in (like len()) or come from libraries

These are procedural-style function calls — you pass the string as a parameter.

isalpha()
isdigit()
isalnum()
islower()
isupper()
startswith()
endswith()
find()          - serches for a value retruns its position
replace()       - replaces one value with aother 

lstrip()        - removes whitespaces from the left of the string including \t
rstrip()        - removes whitespaces from the right of the string including \t
strip()        - removes whitespaces from the left and right of the string including \t

split()     - split the string based on some string 
partition() - partitions the string into 3 parts using the string 

String conversion 
    - converting the case of characters in the string 
        - upper()
        - lower()
        - capitalize()  - converts the first character of each string into uppercase
        - title()       - converts the first character of each word into uppercase 
        - swapcase()

    - converting the numbers to string and vice verca 
        - str()     - converts int, float or complex into string
        - int()
        - float()
        - complex() - converts a numeric string into complex 

String Comparison 
        - string can be compared using the below operators 
        - == , != , > , >= , < , <= 

Byte Sequence 
        - Byte sequence are used to represent the binary data . Since 4 bit binary represent one
        hexadecimal digit, the binary sequence 
        00000000 00000001 00000001 1000001
        00 01 01 81

        >>> a = b'\x81'
        >>> a
        b'\x81'
        >>> 
        >>> int.from_bytes(a,'big')
"""


s = "let us python"
print(type(s))
print(id(s))
print(s.upper())
print(s.lower())


clear_terminal()

"""
Regular Expression 

    - re.search() - scans through the given string , looking for any location where this RE matches
    .If a match is found then re.search() returns a Match object else returns None 

Regex Metacharacters 
    - A regular expression often contains special characters called meta characters
    - [] - . ^ \ * + ? {} | () $

    Metachar []
        - [] used to specify characters class , set of characters that we wish to match 
        print(re.search('[hb]owl' , 'howler' ))
        print(re.search('[hb]owl' , 'bowler' ))
        print(re.search('[hb]owl' , 'cowler'))
    
    Metachar -
        - Metachar "-" is used to define the range of character 
        - [S-Z] -> STUVWXYZ
        - [0-5] -> 012345
    
    Metachar ^
        - metachar ^  is used to complement a character set 
        - RE for checking if any string starts with anything but digit 
        - re.search('[^0-9]', string )

    Metachar |
        - Metachar '|' is used to show alternate between the regular expression 

    Metachar \
        - Metachar '\' is used to escape a metacharacter of it's special meaning  
        - Metachar '\' is also used to introduce special char class like set of digits , set of alphabets or set of white spaces 
        \d  - any decimal digits same as [0-9]
        \D  - any non digit characte same as [^0-9]
        \s  - any whitespace characer [\t\n\r]
        \S  - any non whitespace character [^\t\n\r]
        \w  - any alpha numeric character [a-zA-Z0-9]
        \w  - any non alphanumeric character same as [^a-zA-Z0-9]

    Regex repetetion Qualifiers :
        - It is possible to repeat full or partial regex pattern 
        - Metacharacter used are * + ? {}
        - * represents - character before it can appear zero or more time 
        - + represents - character before it can appeat one or more time 
        - ? represents - character before it can appeat zero or one time 
        - {m} specifies - that exactly m copies of the previous RE should be matched 
        - {m,n} specifies - match preceding RE m to n times 

        Special properties of {m,n}
            - {,n}      -> m is assumed to be 0
            - {m,}      -> n is condidered to be >= m
            - {,}       -> {0,}

    Regex anchors 
        - Anchors are used to specify the location in the search string where a match must occur 
        - Anchor ^ specifies match must be found at the beginning of the string
        - Anchor $ specifies match much be found at the end of the string 

    Regex Grouping 
        - () is used to represent a subexpression in the group
        - 

Note :
    1. Special characters can be retained either by escaping them or making the string as a raw string .
    2. 
"""

import re
s = 'Bombaywala'
print(re.search('bay' , s) ) # <re.Match object; span=(3, 6), match='bay'>


# Match is found id first chatacter is h or b
print(re.search('[hb]owl' , 'howler' ))
print(re.search('[hb]owl' , 'bowler' ))
print(re.search('[hb]owl' , 'cowler'))

# RE for verifiying the 5 digit pin code 
pin = '261141'
if re.search('[0-9][0-9][0-9][0-9][0-9][0-9]', pin):
    print(f"{pin} is valid !!")
else :
    print("Please enter the valid pin code !!")

# RE to check if string starts with anything but digit 
print(re.search('[^0-9]','zebra'))

print(re.search('[^0-9]','9'))

clear_terminal()
# Use of | metchar
print(re.search('[a-z | A-Z]','Zebra') )
print(re.search('[a-z | A-Z| 0-9]','9999') )



print(re.search('[a-z\$]', '$35.8' ))

# Metchar \
print(re.search('\W','__main__'))
print(re.search('[\s,.]','ttt'))

# Regex repetetion Qualifiers :

print(re.search('\d-+\d','444-333'))

print(re.search( '\w*@gmail.com','ac@gmail.com'))
print(re.search( '\w*@gmail.com','@gmail.com'))

# RE for 6 digit pin 
print(re.search('[0-9]{6}','666666'))

# RE for 6 alphanumeric char 
print(re.search('\w{6}','abc98d' ))
print(re.search('\w{6}','abc98' ))


# RE for 6 to 8 alphanumeric char 
print(re.search('\w{6,8}','abcdef'))
print(re.search('\w{6,8}','abcde'))

# Regex Anchors 

print(re.search('^Ram','Rampur' ))
print(re.search('^Ram','rampur'))
print(re.search('pur$','rampur'))
print(re.search('pur$','puri'))



#Regex Grouping 

print(re.search('(fun[cd])','function'))
print(re.search('(fun[cd])+','function'))
print(re.search('fun([cd]){1,3}(on)?','function'))


print("**Execices** " * 5)

ss = 'rishabh'
mls = 'rishabh ... \
shukle'


print(mls)

# mls[1] ='t' # throws error as string are immutable

str1 = 'c:\\temp\newline'
str1 = r'c:\\temp\newline'
print(str1)

msg7 = 'utpia'
msg8 = 'todday'
msg7 = msg7 + msg8
print(msg7)

clear_terminal()
print("Program 4.2")
s = "Bamboozled"
print(s[:2])
print(s[-2:])

print(s[8:])
print(s[2:])
print(s[-8:])

print(s[:-4])
print(s[:6])
print(s[-10:-4])

print(s[::-1])
print(s[0:10:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:4])


clear_terminal()
print("Program 4.3")

s = ['NitiAyog','And Quit Flows The Don','1234567890','Make $1000 a day','1ends with And']

for ip in s :
    if ip.isalpha() : print(f"Is alpha  : {ip}")
    if ip.isnumeric() : print(f"Is Numeric  : {ip}")
    if ip.islower() :print(f"is lower : {ip}")
    if ip.isupper() :print(f"is upper : {ip}")
    if re.search('^And | And$',ip) : print(f"starts/ends with And :{ip}")
    # if re.search('And$',ip) : print(f"starts with And :{ip}")


clear_terminal()
print("Program 4.4")

s1 = "Bring It On"
print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())
print(s1.find('I'))
print(s1.find('O'))
print(s1.replace('It','Him'))

s2 = "  Flanked by spaces on either side    "
print(s2.lstrip())
print(s2.rstrip())

s3 = "C:\\Users\\Kanetkar\\Documents"
s3_raw =r"C:\\Users\\Kanetkar\\Documents"
print(s3)
print(s3_raw)

print(s3_raw.split("\\"))
print(s3_raw.partition("\\"))



clear_terminal()
print("Program 4.5")

ip = "The Terrible Tiger Tore The Towel"

idx = ip.find('T')

while idx != -1 :
    print(f"T is at {idx}")
    idx = ip.find('T',idx+1)

print(ip)
ip2 = ip.replace('T','t',2)
print(ip2)

"""
ip2 = ip.replace('T','t',2)
Third parameter tell the number of characters to be replaced 
"""