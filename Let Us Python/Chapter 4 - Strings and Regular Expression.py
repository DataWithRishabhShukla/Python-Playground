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


clear_terminal()
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
"""


s = "let us python"
print(type(s))
print(id(s))
print(s.upper())
print(s.lower())


