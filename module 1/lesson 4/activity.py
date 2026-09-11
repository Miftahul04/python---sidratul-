field1 = 120
field2 = 85
field3 = 150
field4 = 94
field5 = 110

total = field1 + field2 + field3 + field4 + field5
print(f"Total Harvesting: {total}kg")
average = total/5
print(f"Average harvesting in a field: {average}kg")

price_per_kg = 25
earnings = total * price_per_kg
print(f"Earnings: {earnings}BDT")
bags = total // 25
print(f"Full bags packed: {bags}bags")
leftover = total%25
print(f"Leftover grain: {leftover}kg")