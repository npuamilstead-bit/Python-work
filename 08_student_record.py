student = {"name": "Alex",
           "school": "SCAI",
           "gpa": 3.8,
           "completed_credits": 6}
print("welcome,", student["name"], "enjoy your stay at", student["school"])

student["completed_credits"] += 15
student["standing"] = "Full-Time"
for key, value in student.items():
    print(key,":", value)
