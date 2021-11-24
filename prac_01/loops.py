# 1) odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# 2) count in 10s
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# 3) count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# 4) print n stars.
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# 5) print n lines of increasing stars.
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()
