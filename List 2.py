n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
smallest1 = lst[0]
smallest2 = lst[1]

for el in lst:
    if smallest1 > el < smallest2:
        smallest2 = smallest1
        smallest1 = el
    elif smallest1 < el < smallest2:
        smallest2 = el
print(smallest2)
