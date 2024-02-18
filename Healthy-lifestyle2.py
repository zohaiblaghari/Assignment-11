def calculate_sleep_duration(bedtime, weakup_time):
    bedtime_minutes = bedtime.hour * 60 + bedtime.minute
    wakeup_time_minutes = wakeup_time.hour * 60 + wakeup_time.minute

    sleep_duration_minutes = wakeup_time_minutes - bedtime_minutes

    hours = sleep_duration_minutes // 60
    minutes = sleep_duration_minutes % 60

    return hours,minutes

bedtime_hour = int(input("Enter your bedtime hour (0-23):"))
bedtime_minute = int(input("Enter your bedtime minute (0-59):"))
wakeup_hour = int(input("Enter your wake-up hour (0-23):"))
wakeup_minute = int(input("Enter your wake-up minute (0-59):"))

from datetime import datetime,time 
bedtime = time(bedtime_hour,bedtime_minute)
wakeup_time = time(wakeup_hour,wakeup_minute)
sleep_hours,sleep_minutes = calculate_sleep_duration(bedtime,wakeup_time)

print("Total sleep duration:",sleep_hours,"hours and",sleep_minutes,"minutes.")

recommended_min_hours = 7
recommended_max_hours = 9
if sleep_hours < recommended_min_hours:
    print("you did not get enough sleep. Aim for at least 7 hours of sleep.")
elif sleep_hours > recommended_max_hours:
    print("you got more sleep than recommended. Aim for around 7-9 hours of sleep for optimal health.")
else:
    print("you got the recommended amount of sleep.keep it up!")
