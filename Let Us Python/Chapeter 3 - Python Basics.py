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
    - 

"""
import random 
print(random.randint(10,20) )
print(dir(random))