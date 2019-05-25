name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

inch_cm = 2.54
lbs_kg = 0.4535924

height_cm = round(height * inch_cm)
weight_kg = round(weight * lbs_kg)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall ({height_cm} cm).")
print(f"He's {weight} pounds heavy ({weight_kg} kg).")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} dependign on the coffee.")
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

