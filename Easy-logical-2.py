age = int(input("Enter your age:"))

if age < 13:
    print("you are a child.")
elif age < 20:
    print("you are a teenager.")
elif age < 50:
    print("you are an adult.")
else:
    print("you are a senior citizen.")