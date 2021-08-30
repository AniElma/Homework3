el1 = int(input())
el2 = int(input())
el3 = int(input())
lst = [el1, el2, el3]

lst.sort(reverse=True)
print(lst[0] - lst[-1])
