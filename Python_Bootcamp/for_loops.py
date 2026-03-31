# For Loops in Python
print('Topic: For Loops in Tuple \n')
for i in (1,2,3,4,5):
    print("Round:", i)    # print(f"{Round: {i}"). this form works too

print("_"*20, "\n")

print('Topic: For Loops in List \n')
items = ['apple', 'banana', 'cherry']
for item in items:
    print(f"I bought my favorite {item} from the market.")

print("_"*20, "\n")

print('Topic: For Loops in String \n')
for letter in "Python":
    print("Current Letter:", letter)
   
print("_"*20, "\n")

print('Topic: For Loops with Range Function \n')
for num in range(1, 5):  # range(5) generates numbers from 0 to 4
    print("Number:", num)

print("_"*20, "\n")

scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current Total:", total)
print("Final Total Score:", total)

print("_"*20, "\n")

print("Topic: Data Cleaning with For Loops \n")
files = [" Report.csv", "Data.csv ", " final.TXT "]
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print("Cleaned File Name:", file)

print("_"*20, "\n")

print("For Loop Python Challenge \n")
# Print 7 time tables using a for loop
for number in range(1, 11):
    result = 7 * number
    print(f"7 x {number} = {result}") #print("7 x " + str(number) + " = " + str(result))

print("_"*20, "\n")

print("Pyramid using for loop \n")
for x in range(1, 7):
    y = "*" * (2 * x - 1)
    print(" " * (6 - x) + y)
