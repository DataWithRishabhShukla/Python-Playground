"""
Dictionary 
    - Keys in dictionary must be unique and immutable .
    - Numbers , strings , tuples can be used as key 
    - If you're using the tuple as key , it should not contain any mutable elements like list 
    - If you use list as keys or tuple with list as element , 
        - you get unhashable key error 


"""

from common.common_library import clear_terminal
clear_terminal()
d = {(1,5):'ME126',(3,2):'Me102',[45,6]:'Me2022'}
print(d)