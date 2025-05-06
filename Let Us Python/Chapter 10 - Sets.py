"""
Sets 
    - sets are like lists with an exception that they do not contain duplicate values 
    - creting an empty set 
        - set()
        - {20} # If you leave it empty it will be a dictionary 
    - while storing element in a set , hash value is computed to determine weather it should be stored or not 

    - It is possible to create set of string and tupe but not a set of lists 
        - TypeError: unhashable type: 'list'
        - since string and tuples are immutable , their hash value remains same . Hence sets of string and tuple are permitted 
        - A list may  change , so the value of hash may change . Hence sets of lists are not permitted 


"""

from common.common_library import clear_terminal
from pprint import pprint as p


a = set()
b = {20}
print(a, type(a),b,type(b))


print("Creating the empty set , list , dictionary , tuple !!")


l = []
str = ''
dic = {}
set = set()

print(type(l), type(str) ,type(dic) , type(set))

clear_terminal()
print("It is possible to create set of string and tupe but not a set of lists")

s1 = {'morning','evening'}
s2 = {(19,29),(17,34,34)}
# s3 = {[19,29],[17,34,34]}
print(s1, s2)
# print(s3) # TypeError: unhashable type: 'list'