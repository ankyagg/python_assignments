name =  str(input("Enter your name"))
date = input("Enter the date on which the meeting is going to be conducted")
time = int(input("Enter the time at which the meeting is going to be conducted(24 hour format)"))
if 6<time<12:
    print("Good morning")
elif 12<time<18:
    print("Good evening")
else:
    print("Nice meeting you")
print(f"Welcome Mr {name} welcome , your meeting has been timed for {time} at  date {date}")
