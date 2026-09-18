courses = ["CSE 110", "FSE 100", "Biology 101", "MAT 265"]

for course in courses:
    print("Course: ", course)

credit_list = [3, 2, 4, 3]

total_credits = 0
for i in credit_list:
    total_credits += i
    

print("total credits:", total_credits)
if total_credits >= 12:
    print("Student is full time.")
else:
    print("Student is not full time.")