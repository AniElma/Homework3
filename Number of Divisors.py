x = int(input())
Divisors = 0
for y in range(1, (x+1)):
    if x % y == 0:
        Divisors += 1
print(Divisors)
