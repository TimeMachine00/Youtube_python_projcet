# Welcome to AI-PY youtube Channel

"""
BMI calculator
"""
weight = float(input("enter your weight in kg \n"))

height = float(input("enter your height in meters\n"))

BMI = round(weight/height**2, 2 )

if BMI < 18.5:
    print(f"your BMI is {BMI}, and you are under weight")
elif BMI < 25:
    print(f"your BMI is {BMI}, and you are normal wight")
elif BMI <30:
    print(f"your BMI is {BMI}, and you are  over wight")
elif BMI <35:
    print(f"your BMI is {BMI}, and you are  obese ")
else:
    print(f"your BMI is {BMI}, and you are  clinically obese ")

