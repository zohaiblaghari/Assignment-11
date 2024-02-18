def calculate_calorie_goal(age,weight,activity_level):
    base_calories = 2000

    if age < 18:
        base_calories -= 200
    if weight > 80:
        base_calories += 100

    if activity_level == "simple":
        calorie_goal = base_calories * 1.2
    elif activity_level == "medium":
        calorie_goal = base_calories * 1.5
    elif activity_level == "advance":
        calorie_goal = base_calories * 1.7
    else:
        calorie_goal = base_calories

    return calorie_goal

age = int(input("Enter your age:"))
weight = float(input("Enter your weight in kilograms:"))
activity_level = input("Enter your activity level (simple/medium/advance):")

daily_calorie_goal = calculate_calorie_goal(age,weight,activity_level)
print("your daily calorie goal is:", daily_calorie_goal,"calories.")