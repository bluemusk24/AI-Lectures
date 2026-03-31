#print('hello world')
import random

# example with print, strings and + (concatenation)
hello = 'hello'
name = input("Enter your name: ")
greeting = hello + " " + name
print(greeting)

# example with random
roll = random.randint(1,6)
print('The computer rolled ' + str(roll))
#print(f'The computer rolled {roll}')