a1, b1, a2, b2 = float(input()), float(input()), float(input()), float(input()),
lst1 = [a1, b1]
lst2 = [a2, b2]
lst1.sort()
lst2.sort()

if lst1[1] < lst2[0]:
    print(0)
elif lst2[0] < lst1[1] < lst2[1]:
    print(lst1[1] - lst2[0])
elif lst1[0] > lst2[0] and lst1[1] > lst2[1]:
    print(lst1[1] - lst2[1])
elif lst1[0] < lst2[0] and lst1[0] < lst2[1]:
    if lst1[1] > lst2[0] and lst1[1] > lst2[1]:
        print(float(lst2[1] - lst2[0]))




