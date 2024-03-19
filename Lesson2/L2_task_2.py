def is_year_leap(year):
        if (year%4 == 0):
            return True
        else:
            return False
            
user_year = int(input("Год "))
print (f"Год {user_year}: {is_year_leap(user_year)}")
