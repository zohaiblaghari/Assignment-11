def calculate_water_intake(weight,exercise_level):
    if exercise_level == "light":
        water_intake_liters = weight*0.03
    elif exercise_level == "moderate":
        water_intake_liters = weight*0.04
    elif exercise_level == "intense":
        water_intake_liters = weight*0.05
    else:
        print("Invalid exercise level. please choose from 'light','moderate',or'intense'.")
        return None
    return water_intake_liters

weight = float(input("Enter your weight in kilograms:"))
exercise_level = input("Enter your desired level of hydration (light/moderate/intense):")

water_intake = calculate_water_intake(weight,exercise_level)
if water_intake is not None:
    print("you should drink approximately", water_intake, "liters of water throughout the day.")