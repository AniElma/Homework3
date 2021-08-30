num = int(input())
while num > 0:
    if num < 10:
        print('No')
        break
    elif (num % 10) > ((num // 10) % 10):
        print('Yes')
        break
    else:
     num = num // 10
