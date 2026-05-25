class LeapYear:
    def is_leap_year(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return f"{year} is a leap year"
        return f"{year} is not a leap year"

obj = LeapYear()
year = int(input("Enter year: "))
print(obj.is_leap_year(year))