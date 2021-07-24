import datetime
import sys
print(datetime.date.today())
print(f"Hello + World")
print("344_3445_99")
#print("Hi ," +  input("whats your name? ") + " how are you doing today ?" + " Todays date is :", datetime.date.today())
print(datetime.date.today().strftime("%Y"))

current_age=int(input("Enter your current age: "))
_max_age=90

diff_age_years=90-current_age

print(f"you have {diff_age_years} years or {diff_age_years*365} days or {diff_age_years*12} months or {diff_age_years*52} weeks left!")

print(len(input("Whats your name ? ")))

print("Welcome to Band name generator!")
user_name=input("Whats the name of the city you were born? ")
fav_animal_name=input("Whats your favourite animal? ")

print("your band name could be : " + user_name+ " "+ fav_animal_name)

print("Welcome to bill  calculator")
bill_amount=int(input("What was your total bill? : $"))
people_count=int(input("Number of  people to split the bill against" ))
tip = int(input("Tip percent - 5 or 10 or 15? "))
print("Each person should pay : " + str((bill_amount + (bill_amount*tip/100))/people_count))


