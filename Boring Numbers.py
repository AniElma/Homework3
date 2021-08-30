num = int(input())
while num > 0:
    if num < 10:
        print('Boring')
        break
    elif (num % 10) != ((num // 10) % 10):
        print("Interesting")
        break
    else:
        num = num // 10
