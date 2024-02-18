def find_common_time(availabilities):
    common_times = []
    for time_slot in range(24):
        available = True
        for availability in availabilities:
            if time_slot not in availability:
                available = False
                break
        if available:
            common_times.append(time_slot)
    return common_times

def input_availability(user):
    print(f"Enter {user}'s availability (comma-separated hours, e.g,'9,10,11'):")
    availability_str = input().strip()
    availability = [int(hour.strip())for hour in availability_str.split(',')]
    return availability

def main():
    num_users = int(input("Enter the number of users:"))
    user_availabilities = []
    for i in range(1,num_users + 1):
        user_availability = input_availability(f"User {i}")
        user_availabilities.append(user_availability)
    
    common_times = find_common_time(user_availabilities)
    if common_times:
        print("Common meeting times:")
        for time in common_times:
            print(f"{time}:00 - {time+1}:00")
    else:
        print("No common meeting times available.")

if __name__=="__main__":
    main()