# Create a BMI calculator to get BMI
# Formula:
# The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9.

# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

hInFeet = float(input("Enter your Height (Feet) : "))
# convert feet into meter
hInMeter = hInFeet * 0.3048

weight = float(input("Enter your Weight (KG) : "))

# get bmi
bmi = weight / (hInMeter * 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi} it's Underweight.Eat healthy food regulerly.")
elif bmi <= 24.9:
    print(f"Great!! Your BMI is {bmi}. You are Healthy.")
elif bmi <= 29.9:
    print(f"Oops! Your BMI is {bmi} it's Overweight, Please control yourself")
else:
    print("Something went worng!!!")
