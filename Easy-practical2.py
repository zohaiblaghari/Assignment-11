def should_wear_jacket(temperature):
    if temperature < 20:
        print("it is cold! you should wear a jacket.")
    else:
        print("The temperature is fine. No need for a jacket")

temperature = float(input("Enter the current temperature in celsius:"))
should_wear_jacket(temperature)