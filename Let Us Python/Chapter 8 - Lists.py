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
 

"""

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
clear_terminal()
lst = [1,2,3,4]
lst = lst + [5,6,7]
print(lst)

# Merging two list 
s = [1,2,3]
t = [5,6,7]
z = s + t
print(z)