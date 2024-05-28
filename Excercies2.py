import time

currentTime = time.strftime("%H:%M:%S")
currentTime = time.strptime(currentTime, "%H:%M:%S")
print(currentTime)

if 5 <= currentTime.tm_hour < 12:
    print("Good Morning")
elif 12 <= currentTime.tm_hour < 17:
    print("Good Afternoon")
elif 17 <= currentTime.tm_hour < 20:
    print("Good Evening")
else:
    print("Good Night")

