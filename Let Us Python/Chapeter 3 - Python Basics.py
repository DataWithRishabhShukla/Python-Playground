"""
There are 33 keywords in the python 
Variable can start with _ or alphabet 
"""

from common.common_library import clear_terminal


clear_terminal()
import keyword
print(keyword.kwlist)

"""
Python has built-in functions , 
print - it is used to send the output to screen
description about function can be done using help(func)

Built-in Modules 
    - Apart from functions , python has built in modules 
    - Each module has functions that can be used 
    - To  use functions defined in a module , you need to import it 
    - it's normal to forget the name of the function defined in the module , we can use the dir function 
        - print(dir(random))

Container Types
    - list - collection of similar or disimilar elements 
    - tupe - collection of immutable type 
    - set - collection of unique elements
    - dictionary - collection of key:value pairs

    - Values in list and tuple can be accessed using their position 
    - Values in set can be accessed using the for loop 
    - Values in the dictionary can be accesses using the keys 

Python Jagrons 
    - Collection - generic term for collections 
    - iterable      - means collection whose element can be iterated using the loop
    - ordered Collection 
        - Elements are stored in the same order in which they are inserted
        - Since position is fixed they can be asssecced using the index 

    - Unordered Collection 
        - Elements are not stored in the same order in which they are inserted
        - Can not be accessed using the index 

    - Sequence - Another name for the ordered collection 
    - Mutable   - means values can be changed
    - Immutanle - means values cannot be changed 

    List - ordered collection , iterable , mutable 
    Strings -  ordered collection , iterable , immutable 
    Tuple - ordered collection , iterable , immutable 
    Sets - unordered collection , iterable , mutable
         - Because you can add or remove from the sets [add , remove ]
    dict - unordered collection , iterable , mutable 



"""
from common.common_library import clear_terminal

import random 
print(random.randint(10,20) )
print(dir(random))

import random
import time

clear_terminal()
current_seed_time = int(time.time()* 1000)
print(f"{current_seed_time = }")

a, b = 5,10
a,b = b,a
print(a,b)

random.seed = 20
for i in range(5):
    print(random.randint(10,50))
    # random.seed += random.randint(10,50)
    
    
