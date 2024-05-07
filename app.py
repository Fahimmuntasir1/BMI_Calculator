# Create a BMI calculator to get BMI
# Formula:
# The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9.

hInFeet = float(input("Enter your Height (Feet) : "))
# convert feet into meter
hInMeter = hInFeet * 0.3048

weight = float(input("Enter your Weight (KG) : "))

# get bmi
bmi = weight / (hInMeter * 2)
print(bmi)
