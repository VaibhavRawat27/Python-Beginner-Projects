def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

height = float(input("Enter height in cm: "))
weight = float(input("Enter weight in kg: "))

bmi_result = calculate_bmi(height, weight)
print(f"Your BMI is: {bmi_result}")

if bmi_result < 18.5:
    print("You are Underweight.")
elif 18.5 <= bmi_result < 24.9:
    print("You have Normal weight.")
elif 25 <= bmi_result < 29.9:
    print("ou are Overweight.")
else:
    print("You are Obese.")
