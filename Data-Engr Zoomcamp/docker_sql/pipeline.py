import sys

import pandas as pd

# do some fancy stuff with pandas like loading a csv file

print(sys.argv)

day = sys.argv[1]
num = sys.argv[2]
greet = sys.argv[3]


print(f'job successfully executed for day = {day}')
print(f'i made ${num} working on this particular day {day}')
print(f'I said {greet} to my boss on this day {day} for the ${num} paycheck') 
