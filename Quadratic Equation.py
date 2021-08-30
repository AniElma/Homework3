a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4*a*c
x1 = (-b+D**1/2)/2*a
x2 = (-b-D**1/2)/2*a

if a == 0 and b != 0:
    print('Non-quadratic equation')
    x1 = -c/b
    print('One solutions: {}'.format(x1))
elif a == b == 0 and c != 0:
    print('Non-quadratic equation')
    print('No Solutions')
elif a == b == c == 0:
    print('Non-quadratic equation')
    print('Infinite solution')

elif a != 0:
    print('Quadratic equatin')
    if D < 0:
        print('Discriminant: {}'.format(D))
        print('No Solutions')

    elif D > 0:
        print('Discriminant: {}'.format(D))
        print('Two solutions: {}'.format(x1), '{}'.format(x2))

    else:
        print('One solutions: {}'.format(x2))
        print('Discriminant: {}'.format(D))



