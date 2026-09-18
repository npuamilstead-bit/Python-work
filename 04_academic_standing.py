GPA = float(input("What is your GPA? "))
credits_taken = int(input("How many credits are you taking? "))

if GPA >= 3.5 and credits_taken >= 12:
    print("You made the Dean's List!")
elif GPA >= 3.5 and credits_taken < 12:
    print("Not enough credits for the Dean's List, You have made the Dean's List Commendation!")
elif GPA >= 2.0 and GPA < 3.5:
    print("You are in good academic standing.")
else:
    print("You are in academic probation.")