# Welcome to AI-PY youtube Channel

"""
leap year calculator
"""
year = int(input("enter the year to check\n"))

if year %4 ==0:
    if year%100==0:
        if year%400==0:
            print("it is leap year")
        else:
            print("it is not a leap year")

    else:
        print("it is a leap year")



else:
    print('it is not a leap year')

