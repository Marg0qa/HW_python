side = int(input("сторона="))

import math
def square(side):
    area = side * side
    area = math.ceil(area)
    return area

print(f"Площадь квадрата равна {square(side)}")