# Welcome to AI-PY youtube Channel

"""

Love calculator
"""
name1 = input("enter your name\n").lower()
name2 = input("enter your partner name\n").lower()

T1,T2 = name1.count('t'), name2.count('t')
R1, R2 =name1.count('r'), name2.count('r')
U1, U2= name1.count('u'), name2.count('u')
E1,E2 = name1.count('e'),name2.count('e')

a =str(T1+T2+R1+R2+U1+U2+E1+E2)

L1,L2 = name1.count('l'),name2.count('l')
O1,O2 =name1.count('o'),name2.count('o')
V1,V2 = name1.count('v'),name2.count('v')
E11,E22 =name1.count('e'),name2.count('e')

b = str(L1+L2+O1+O2+V1+V2+E11+E22)

total =int(a+b)


if total>80:
    print(f"your love score is{total}%, ureka you can go for honey-moon")
elif total>=40 and total<=70:
    print(f"your love score us {total}%, you are alright")
else:
    print(f"your love score is {total}%")