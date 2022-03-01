# Simple BMI calculator which will tell you your BMI index and interprets it
# <18.5       -> underweight
# 18.5 - <25  -> normal weight
# 25 - <30    -> slightly overweight
# 30 - <35    -> obese
# 35+         -> clinically obese

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you are obese.")
else:
  print(f"Your bmi is {bmi}, you are clinically obese.")
