x=int(input('вклад= '))
y=int(input('срок вклада= '))
import math
def bank(x, y):
    total = x
    for i in range(y):
        total += total * 0.10
    return total
result = math.floor(bank(x, y))
print((f"Сумма на счету после {y} лет будет составлять: {result} рублей"))