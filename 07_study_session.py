target_hours = 20
logged_hours = 0

while logged_hours < target_hours:
    daily_hours = float(input("Enter hours studied today (or -1 to quit early): "))
    if daily_hours == -1:
        print("Session cancelled early.")
        break
     
    logged_hours += daily_hours
    print(f"Logged: {logged_hours}/{target_hours} hours.")
if logged_hours >= target_hours:
    print("Target reached! Ready for SCAI exams!")
else:
    print(f"Session ended with {logged_hours} total hours.")

