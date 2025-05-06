"""
Dictionary 
    - Keys in dictionary must be unique and immutable .
    - Numbers , strings , tuples can be used as key 
    - If you're using the tuple as key , it should not contain any mutable elements like list 
    - If you use list as keys or tuple with list as element , 
        - you get unhashable key error 
    
Dictionary can be nested .  
    - 

Merging Dictionary 
    - Two dictionary can be merged to create a third dictionary 
    - By unpacking the dict using **
    -  if we use * then only keys will be unpacked , set will be created 


"""

from common.common_library import clear_terminal


# d = {(1,5):'ME126',(3,2):'Me102',[45,6]:'Me2022'} # TypeError: unhashable type: 'list'

d = {(1,5):'ME126',(3,2):'Me102'}
print(d)

# Dictionary can be nested 

contacts  = {
    'Anil':{'dob':'17/11/98','favorite':'igloo'},
    'rishabh':{'dob':'10/010/93','favorite':'tundra'}
}

print(contacts['Anil']['favorite'])

# Two dictionary can be unpacked using **

animals = {'tiger':141, 'lion':152,'leopard':110}
birds = {'eagle':38,'parrot':2}

combined = {**animals, **birds}
print(combined)

combined_str = {*animals, *birds}
print(combined_str)
print(type(combined_str))


clear_terminal()

print('Page = 144 Exercise = 11.1')
students = {'rish':30,'charu':45}
stud = students

students = {}
# students.clear() 
print(stud)

clear_terminal()

print('Page = 144 Exercise = 11.2')
cricketrs = ['rohit', 'rahul', 'bumrah']

d = dict.fromkeys(cricketrs,50)
print(d)

clear_terminal()

print('Page = 145 Exercise = 11.3')

d = {'oil':230, 'clip':150, 'stud':175, 'nut':35}

print('Sort by keys in ASC and DSC order')
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),reverse = True)))

print('\n\nSort by values in ASC and DSC order')
print(dict(sorted(d.items(),key = lambda x : x[1])))
print(dict(sorted(d.items(),key = lambda x : x[1],reverse = True)))
print(d)


clear_terminal()

print('Page = 146 Exercise = 11.4')
d1 = {'mango':20,'guava':15}
d2 = {'apple':20,'banana':15}
d3 = {'kiwi':20,'pineapple':15}

d4 = {**d1, **d2, **d3}
print(d4)

d5 = {}
for d in (d1, d2, d3):
    d5.update(d)

print(d5)

# check if dict is empty or not 
d5 = {}

clear_terminal()
if not d5 :
    print("Dict is empty")


# find the maximum and minimum salary
clear_terminal()
d = {
    'anuj':{'salary':10000,'age':20, 'height':6},
    'aditya':{'salary':6000,'age':20, 'height':6},
    'rahul':{'salary':7000,'age':20, 'height':6},
}

max_sal , min_sal = float('-inf') , float('inf')

for name in d :
    max_sal = max(max_sal,d[name]['salary'])
    min_sal = min(min_sal,d[name]['salary'])

print(f"{max_sal=} {min_sal=}")

