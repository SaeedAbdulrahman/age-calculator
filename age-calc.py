from datetime import date
import os

os.system('clear')

print("Please input the following: (DOB)\n")
day = input("Day [1-31]: ")
month = input("Month [1-12]: ")
year = input("Year: ")

def calcage(dob):
    age = int((date.today() - dob).days / 365.2425)
    return str(age)

print("\nYou are " + calcage(date(int(year), int(month), int(day))) + " years old.")
