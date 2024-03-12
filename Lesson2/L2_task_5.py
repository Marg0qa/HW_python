
def month_to_season(a):
    if a >= 1 and a <= 12:
        return ("зима")
    elif a >= 3 and a <= 5:
        return("весна")
    elif a >= 6 and a <= 8:
        return("лето")
    elif a >= 9 and a <= 11:
        return("осень")
    else:
        return("укажите правильный номер месяца")
print(month_to_season(int(input("номер месяца "))))


# можно так же составить через оператора OR. Например: a == 1 or a == 2 or a == 12