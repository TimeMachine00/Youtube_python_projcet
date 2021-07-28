# Welcome to AI-PY youtube Channel

"""

pizza bill calculator
"""
size = input("choose piza size: S, M, L\n")
add_pepporoni = input("do you want pepporoni: yes or no\n")
cheese = input("do you want extra cheese: yes or no\n")

bill = 0

if size == 'S':
    bill+= 200
elif size =='M':
    bill+=250
elif size == "L":
    bill+=300


if add_pepporoni=='yes':
    if size == 'S':
        bill+=20
    else:
        bill+=30
if cheese=='yes':
    bill+=10
print(f"your bill is {bill}")