print("Topic: Nested Loops \n")
for x in range(3):    # Outer loop
    for y in range(2):  # Inner loop
        print(f"({x}, {y})")

print("__" * 20)

for x in range(3):    # Outer loop
    for y in range(2):  # Inner loop
        for z in range(2):  # Innermost loop
            print(f"({x}, {y}, {z})")

print("__" * 20)

print("Real World Examples: \n")
colors = ["Red", "Green", "Blue"]
sizes = ["S", "M", "L"]
for color in colors:
    for size in sizes:
        print(f"Product: {color} - Size: {size}")

print("__" * 20)

years = [2026, 2027]
months = ["Jan", "Feb", "Mar"]
days = range(1, 4)  # Days 1 to 3
for year in years:
    for month in months:
        for day in days:
            print(f"report_{day}_{month}_{year}.csv")

print("__" * 20)

tables = ["customer", "orders", "products", "prices", "discounts"]
columns = ["id", "name", "email"]
for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} WHERE {c} is NULL;")