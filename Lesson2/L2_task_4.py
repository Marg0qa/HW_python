n=int(input("max "))
for b in range(1, n+1):
    if b % 3 == 0 and b % 5 == 0:
        print('FizzBuzz')
    elif b % 3 == 0:
        print('Fizz')
    elif b % 5 == 0:
        print('Buzz')
    else:
        print(b)
