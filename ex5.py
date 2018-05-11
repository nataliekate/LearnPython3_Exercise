name = 'Natalie'
age = 30 # that's a lie
height = 180 # cm
weight = 74 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"She's {height} centimeters tall.")
print(f"She's {weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee and tea.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

# convert centimeters to inches
height_in_inches = round(height * 0.39370)

# convert kilograms to pounds
weight_in_lbs = round(weight / 0.45359237)

print(f"Her weight is {weight_in_lbs} pounds and height is {height_in_inches} inches.")