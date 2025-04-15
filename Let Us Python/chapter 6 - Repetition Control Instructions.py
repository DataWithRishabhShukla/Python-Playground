
from common.common_library import clear_terminal

"""
Repetition Control Instructions 
    - It helps in reapeating a set of instrcutions in a program 
        - while 
        - for 

while loop 
    - while loop is used to repeat set of instructions as long as condition is true 
    - else block is optional , it is executes when condition fails 
    - If loop is terminated abruptly , else block won't be executed 

for loop 
    - for is used iterate over elements of a sequence such as list, strings, tuple or set 

Usage of while loop - 3 Use Cases 
    - Repeat a set of instruction till condition is True 
        - In this case we don't knoe how many time loop will be executed beforeahand 
    - Repeat a set of statements a finite number of times 
    - Iterate through a string , list or tuple 
    - Since values in the sets and dictionary can not be accesses using the index value , it 
    is better to use the for loop for the iteration 
    - Out of all three use cases listed above for loop is more appropriate for first two 

"""
clear_terminal()
# while loop use case - 1 
num = 10

while num != 5 :
    print(num, num**2)
    num = int(input("Enter the number : "))

# while loop use case - 2
count = 1

while count <= 4:
    print(count, count ** 2)
    count += 1

# while loop use case - 3
s = "mumbai"
lst = [1,2,3,4,5,6]
tpl = (10,20,30,40,50,60)
i = 0 
while i <len(s):
    print(s[i],lst[i],tpl[i])
    i += 1
