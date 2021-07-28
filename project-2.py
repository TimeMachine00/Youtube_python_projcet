# Welcome to AI-PY youtube Channel
"""
A group of people let say five goes to foreign trip and they also take a oth to donate some percentage of money
over their overall tour expenses
In this project we create calculator that can calculate foreign tour expenses for each person with donation

"""

totalExpenses= int(input("total amount for this tri?\n"))

percentage_of_donation = int(input("what percentage of total ampount would you like to donate?\n"))

total_number_of_person = int(input("how many persons are going to this trip?\n"))

donation = percentage_of_donation/100 * totalExpenses

total_amount = totalExpenses+donation

amount_for_each_person = total_amount/total_number_of_person

print(f"amount for each person for this trip is: {amount_for_each_person}")

