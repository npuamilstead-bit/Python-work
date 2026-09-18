user_name = input("What's your name? ")
user_credits = input("How many credits are you planning on taking this semester?")
semesters_credits = (120/int(user_credits))
print(f"Hello, {user_name}, you are taking {user_credits} credits this semester. It will take you {semesters_credits} semesters to complete your degree.")