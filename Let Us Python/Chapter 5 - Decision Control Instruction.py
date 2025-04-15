"""

Sequence of execution of instructions can be altered using.
    - Decision control instruction 
    - Repetetion control instruction 

Condition is built using ralation operator < , > , <= , >= , == , != 

Logical Operators 
    - complex decisions can be made using logical operators and , or , not 

    - AND operator evaluates ALL expression. It returns last expression if all expressions evaluates
    to true . Otherwise , it returns first value that evalutes to False .

    - OR operator evaluates all expreseeion . It returns first value that evaluates to True .
    Otherwise it returns last value that evalutes to False 

    - If operator requires only 1 operand it's called Unary Operator --  not 
    - If it needs two it's called binary operator -- + , - , * , /

Conditional Expresesion 
    - <expr1> if <conditional_expression> else <expr2>
        - conditional_expression is evaluated first . If it's true expression evaluates to expr1
        otherwise to expr2

all() and any()
    - Instead of using the and , or operators , we can use the built-in function all() , any() to 
    get the same effect .

    - NOTE - all() and any() both recieve a single parameter of type string, list , tuple, set or 
    dictionary . We have passed a tupe of 3 conditions to them. If argument is dict , it is 
    checked wheather keys are True or False .

    a,b,c = 10,20,30
    res = all(( a > 5, b > 20,c > 15)) # False
    res = any((a > 5,b > 20,c > 15 )) # True 

Receiving Input 
    - The way print() function is used to output values on screen , input() built-in function
    can be used to receive input values from the keyboard.
    
    - input() returns a string , if we wish to perform the airthmetic on the number intered 
    we need to convert the string into int , float .

"""
from common.common_library import clear_terminal
print("Start of the chapter 5!!!")
clear_terminal()

print("Exercises ")
# a = int(input("Enter the val of A : "))
a = 20
b = 20 if a < 10 else 30 
print(a,b)

print("a,,b are equal") if a == b else print("a,b are not equal ")

clear_terminal()

i,j,k = 4,-1,0
w = i or j or k
x = i and j and k 
y = i or j and k 
z = i and j or k 
print(f"{w = }")
print(f"{x = }")
print(f"{y = }")
print(f"{z = }")


a = 10 
b = not not a 
print(f"{not a } {not not a }")
print(f"{b = }")


clear_terminal()

a = 10 
if a == 30 or 40 or 60 :
    print('hello')
else :
    print("hi")
