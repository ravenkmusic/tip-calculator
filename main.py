#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? ")
tip = input("What percentage do you want to tip between 10, 12, or 15? ")
number_of_guests = input("How many people are splitting the bill? ")

bill = float(total_bill)
tip_amount = float(tip) / 100
guests_number = int(number_of_guests)

final_bill = round(((bill * tip_amount) + bill) /guests_number, 2)

result = f"Each person should pay ${final_bill}"

print(result)