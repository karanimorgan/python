def leap_year(year):
    # if the year is divisible by 4,it's not a leap year
    # if the year is divisible by 4 but not by 100,its a leap year
    # if the year is divisible by 100, check if its also divisible by 400
    # if the year is divisible by 100 but not by 400 its not a leap year
    if year % 4 != 0:
        print(f"{year}is not a leap year")
    elif year % 100 != 0: 
        print(f"{year}is a leap year") 
    elif year % 400 == 0:
        print(f"{year}is a leap year")
    else:
        print(f"{year} is not a leap year")

if __name__ == "__main__":
    leap_year(2020)
    leap_year(2022)
    leap_year(2025)
    leap_year(2030)

    