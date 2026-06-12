def is_leap_year(year):
    # Write your code here. 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    # Don't change the function name.

print(is_leap_year(2000))
print(is_leap_year(2001))
print(is_leap_year(2002))
print(is_leap_year(2003))
print(is_leap_year(2004))
print(is_leap_year(2005))
print(is_leap_year(2006))
print(is_leap_year(2007))