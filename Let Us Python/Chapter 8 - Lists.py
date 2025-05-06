from common.common_library import clear_terminal

"""
Container 
        - is an entity which contains multiple data types 
        - also called collection or compound data type 
        - Python has following type containers
            - Lists , Tuples , Sets , Dictionary 

Lists 

    - Mutable , ordered , Iterable 
    - A list can grow on shrink during the execution of program , hene it's called dynamic array
    - Like printing * can be used to repeat element multiple times
        - num = [10] * 5  # [10, 10, 10, 10, 10]

Accessing lists 
    - Using for or while loop 
    - While accessing the element if you want to keep track of index , we can use enumerate 
        - for idx,num in enumerate(nums): print(f"{idx =} {num =}")

Basic List Operations 
    - Unlike string lists are mutable 

Concatination 
    - using "+" 

Merging two list 
    - res = lst1 + lst2

Conversion of list 
    - A string/tuple / set can be converted into list using list()

Aliasing 
    - On assiging one list to another , both refer to the same list
    - Changing one changes another 
    - This is also called shallow copy or aliasing 

    
Cloning / deep_copy
    - This involves copying content of one list into another 
    - Both will different list although they contain same values 
    - Also called deep_copy

Searching
    - using the "in" operator 

Identity 
    - Weather two variables are referring two the same list can be checked using "is"

Comparison 
    - It is possible to compare the content of two lists 
    - Comaprison is item by item till there is mismatch 

Emptiness
    - if not []

Built-in functions
    - len() , max() , min() , sum() , any() , all() , 
    - del()         - Deletes element or slice or entire list  - del(lst[2:5])
    - sorted(lst)   - returns sorted list , lst remains unchanges
    - reversed(lst) - used for reversing list 

If multiple variables are referring to the same list , then deleting one does not delete othes 

List Methods 
    - Any list is an object of class list 
    - It's method can be accessed using the syntax - .method()
    - append()
    - remove()  - removes item from list thrown ValueError if value not present 
    - pop()     - Removes last item from the list 
    - insert(2,11)  - Inserts 11 at the position 2
    - .index()      - returns first index of the element passed 

Sorting and Reversing 
    - .reverse()
    - .sort()
        - Both do not return a list 
        - Sort the element in-place 
    - .sort(reverse= True)

Stack DS
    - Follows LIFO
    - We can use list for this 
    - pop()
    - append()

Queue DS 
    - FIFO 
    - Can't use list as deleting from front will require us to shift all the elements by 1 pos
    - We can use the deque for this 
        from collection import deque 


"""
import time 



# Sorting and Reversing 
lst = [20,10,30,40]
print(sorted(lst,reverse=True))
print(lst)
lst.sort()
print(lst)


# If multiple variables are referring to the same list , then deleting one does not delete othes 
lst1 = [1,2,3]
a = b = c = lst1
lst1 = []
print(a,lst1)



a = [1,2,3]
print(list(reversed(a)))
print(a)



# Emptiness
lst = []
if not lst:
    print("empty list ")



# Comparison
a = [1,2,3]
b = [1,2,5]
print(a<b)



# Identity 
lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]
lst3 = lst1 

print(lst1 is lst2) # False 
print(lst1 is lst3) # True 
print(lst1 is not lst2) # True






#Cloning / deep_copy
lst1 = [1,2,4]
lst2 = [] + lst1
print(id(lst1))
print(id(lst2))

lst1[1] = 10000
print(lst1)
print(lst2)



# Aliasing
lst1 = [10,20,30,40,50]
lst2 = lst1 
print(lst1)
print(lst2)
lst1[0] = 100000
print(lst1)
print(lst2)



nums = [10,20,30,40]

num = [10] * 5  # [10, 10, 10, 10, 10]
print(num)

# accesing using while 
i = 0 
while i < len(nums):
    print(nums[i])
    i += 1

for idx,num in enumerate(nums): print(f"{idx =} {num =}")


# Basic List Operations 

animals = ['parrot','zebra', 'cat']
animals[2] = 'lions'

ages = [10,20,30,40,50]
ages[2:4] = [11,11,11]
print(ages)
ages[2:4] = [] # deletes the element from index 2 to 4
print(ages)

# Concatination

lst = [1,2,3,4]
lst = lst + [5,6,7]
print(lst)

# Merging two list 
s = [1,2,3]
t = [5,6,7]
z = s + t
print(z)

# 


######################### Exercises ################################

names = ['anil', 'amol' ,'aditya', 'avi','alka']
print(names)
names.insert(2,'anuj')
print(names)
names.append('zulu')
print(names)
names.remove('avi')
print(names)
idx = names.index('anil')
names[idx] = 'AnilKumar'
print(names)
names.sort()
print(names)
print(sorted(names,reverse=True))



print("Problem 8.2")

odd = [1,3,5,7,9]
even = [2,4,6,8,10]

comb = odd + even 
print(comb)
# comb.insert(0,)

comb = [11,17,29] + comb
print(comb)
print(len(comb))
print(comb)
comb[10:] = [100,200,300]
print(comb)

del(comb[:])
print(comb)
del comb
# print(comb)



clear_terminal()
print("Problem 8.4")

from collections  import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print(q)
q.popleft()

q.popleft()
print(q)



print("Problem 8.5")

import random

lst = []
for _ in range(20):
    num = random.randint(10,100)
    lst.append(num)

print(lst)
print(len(lst))

for ele in lst :
    if ele >= 20 and ele <= 50 :
        lst.remove(ele)

print(lst)
print(len(lst))

clear_terminal()
print("Problem 8.6")

odd = [1,3,5,7,9]
even = [2,4,6,8]
odd[2] = even

print(odd)

flatten = []

for ele in  odd:
    if isinstance(ele,list):
        flatten.extend(ele)
    else :
        flatten.append(ele)

print(flatten)
flatten.sort()
print(flatten)


clear_terminal()

nums = [random.randint(1,10) for _ in range(20)]
print(nums)
key = int(input("Enter : "))

pos = [ idx for idx, val in enumerate(nums) if val == key ]
print(pos)

 
