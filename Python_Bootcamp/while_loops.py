# To repeat a block of code over and and over as long as the condition is true.
print("Topic: While Condition \n")
count = 1 # initialization
while count <= 5:  # condition
    print(f"Count is: {count}")
    count += 1  # update increment

print("__" * 20)

answer = ""
while answer != "yes":
    answer = input("Do you want to exit? (yes/no/maybe): ").lower()
print("Exited the loop.")

print("__" * 20)

print("Topic: While True with Break Statement (Infinite Loop) \n")  # Conditions always runs until break statement is encountered.
while True:
    response = input("Type 'exit' to break the loop: ").lower()
    if response == "exit":
        print("Breaking the loop.")
        break
    else:
        print("You typed:", response)

print("__" * 20)

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ").lower()
    if answer == "yes":
        print("Thank you for agreeing!")
        break
    attempts += 1
else:
    print("No more attempts left.")
