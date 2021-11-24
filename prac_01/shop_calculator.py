
total = 0
number = int(input("number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("number of items: "))
for i in range(number):
    price = float(input("price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("total price for ", number, " items is $", total, sep='')


print("total price for {} items is ${:.2f}".format(number, total))