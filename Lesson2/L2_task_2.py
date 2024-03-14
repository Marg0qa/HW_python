is_year_leap = [2000, 2001, 2002,2003,2004,2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,  2020, 2021, 2022, 2023, 2024]
for y in is_year_leap:
        if (y%4 ==0):
            print(y)

is_year_leap = input("Год ")
result = (int(is_year_leap)%4==0)
print(f"Год {is_year_leap}: {result}")


