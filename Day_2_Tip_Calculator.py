""" Tip calculator """
print("Welcome to the tip calculator!")
total_bill = float(input("What is the total bill amount?\n$:"))
percent = float(input("How much tip would you like to give?\nPercent:"))
person = int(input("How many person to split the bill?\nPerson:"))
final_amount = (total_bill+(total_bill*15)/100)/4
print("Each person should pay: {}".format(final_amount))