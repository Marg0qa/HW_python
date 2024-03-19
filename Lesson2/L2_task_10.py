sum=int(input('вклад= '))
year=int(input('срок вклада= '))
import math
def bank(sum, year):
    total = sum
    for i in range(year):
        total += total * 0.10
    return total
result = math.floor(bank(sum, year))
print((f"Сумма на счету после {year} лет будет составлять: {result} рублей"))