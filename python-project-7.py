# Welcome to AI-PY youtube Channel

"""

Fiding a Key to open Tressure box

"""
import random
path = ['right', 'left']
path_choice = random.choice(path)
# print(path_choice)

wait_or_swim = ['wait','swim']
wait_or_swim_choice =random.choice(wait_or_swim)
# print(wait_or_swim_choice)

room = ['red', 'blue', 'green', 'yellow']
room_choice= random.choice(room)
# print(room_choice)

print("welcome to stage one to find key")

path_select = input("which path do you like to choose: right or left\n").lower()

if path_select!=path_choice:
    print("you have choosen wrong path, and now you are a meal for evel")
elif path_select==path_choice:
    print("welcome to second stage you made it")
    swim_select = input("do you like to swim or wait for some time: enter swim or wait\n").lower()
    if swim_select!= wait_or_swim_choice:
        print("you have taken wrong decission, now are the meal for evil")
    elif swim_select==wait_or_swim_choice:
        print("welcome to stage three, you made it and you are one step far for a key")
        room_select = input("select the proper room color to get a key: red, blue, green, or yellow\n")
        if room_select!=room_choice:
            print("you had selected wrong room, now you will become the evil")
        elif room_select==room_choice:
            print("urekha, you made it, you found proper room to the key..go and get it")

