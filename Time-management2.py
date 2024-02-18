import time

def promodoro_timer():
    work_duration = 25*60
    break_duration = 5*60

    while True:
        print("Work for 25 minutes.")
        time.sleep(work_duration)
        print("Take a 5-minute break.")
        time.sleep(break_duration)

        choice = input("Would you like to continue another promodoro session? (yes/no):").lower()
        if choice != "yes":
            break

print("Welcome to the promodoro timer!")
promodoro_timer()
print("Promodoro session ended. Have a productive day!")