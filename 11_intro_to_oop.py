# Lesson 4.1 & 4.2: The OOP Blueprint (Classes, __init__, and Methods)

class Student:
    def __init__(self, name, school, gpa=0.0):
        # 1. State / Attributes (What a Student 'has')
        self.name = name
        self.school = school
        self.gpa = gpa
        self.completed_credits = 0

    # 2. Behavior / Methods (What a Student 'can do')
    def add_credits(self, credits):
        self.completed_credits += credits

    def update_gpa(self, new_gpa):
      if new_gpa < 0.0 or new_gpa > 4.0:
          print("Invalid GPA.")
      else:
          self.gpa = new_gpa
          print("GPA updated successfully.")
    def is_honors(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False    
  

    def display_profile(self):
        print(f"Student: {self.name} | School: {self.school} | GPA: {self.gpa} | Credits: {self.completed_credits}")

    def __str__(self):
        return f"student: {self.name} ({self.school}) - GPA: {self.gpa:.2f}"
# --- Testing our Blueprint ---
# Instantiate two unique student objects from the same class blueprint:
student_1 = Student("Alex", "SCAI", 3.8)
student_2 = Student("Jordan", "Fulton", 3.5)

student_1.add_credits(15)
student_2.add_credits(12)

student_1.display_profile()
student_2.display_profile()

student_1.update_gpa(3.9)
student_2.update_gpa(4.5)

print(f"{student_1.name} Honors: {student_1.is_honors()}")
print(f"{student_2.name} Honors: {student_2.is_honors()}")

print(student_2)

class OnlineStudent(Student):
    def __init__(self, name, school, gpa, timezone):
        super().__init__(name, school, gpa)
        self.timezone = timezone
        self.proctored_exams_passed = 0
    def pass_exam(self):
        self.proctored_exams_passed += 1
        print(f"{self.name} passed a proctored exam!")

online_student = OnlineStudent("Taylor", "SCAI", 3.6, "MST")

print(f"Credits earned: {online_student.completed_credits}")
print(f"Exams Passed: {online_student.proctored_exams_passed}")