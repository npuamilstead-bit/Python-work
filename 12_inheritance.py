# Lesson 4.3: Inheritance & Reusability (`super()`)

# --- Parent (Base) Class ---
class Student:
    def __init__(self, name, school, gpa=0.0):
        self.name = name
        self.school = school
        self.gpa = gpa
        self.completed_credits = 0

    def add_credits(self, credits):
        self.completed_credits += credits

    def is_honors(self):
        return self.gpa >= 3.5

    def __str__(self):
        return f"Student: {self.name} ({self.school}) - GPA: {self.gpa:.2f}"


# --- Child (Derived) Class ---
# GraduateStudent "is a" Student, so it inherits everything from Student:
class GraduateStudent(Student):
    def __init__(self, name, school, gpa, thesis_topic):
        # 1. Let the parent (Student) initialize name, school, and gpa:
        super().__init__(name, school, gpa)
        
        # 2. Add attributes unique to GraduateStudent:
        self.thesis_topic = thesis_topic
        self.thesis_approved = False

    def approve_thesis(self):
        self.thesis_approved = True
        print(f"Thesis '{self.thesis_topic}' has been approved!")

    # Override: In grad school, honors requires a higher bar (GPA >= 3.8)
    def is_honors(self):
        return self.gpa >= 3.8 and self.thesis_approved

    def __str__(self):
        status = "Approved" if self.thesis_approved else "Pending"
        return f"GradStudent: {self.name} | Thesis: '{self.thesis_topic}' [{status}] | GPA: {self.gpa:.2f}"


# --- Testing Inheritance ---
undergrad = Student("Alex", "SCAI", 3.7)
grad = GraduateStudent("Morgan", "SCAI", 3.85, "Autonomous Drone Swarms")

print(undergrad)
print(grad)

# Notice grad student can use methods inherited from Student:
grad.add_credits(9)
print(f"Grad Credits: {grad.completed_credits}")

# Testing the overridden is_honors() logic:
print(f"Undergrad Honors (GPA 3.7): {undergrad.is_honors()}")
print(f"Grad Honors before thesis approval: {grad.is_honors()}")

grad.approve_thesis()
print(f"Grad Honors after thesis approval: {grad.is_honors()}")
