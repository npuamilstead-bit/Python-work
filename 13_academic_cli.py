# Project 1: SCAI Academic Management CLI System
# ===============================================
# Architecture:
# - Student (Base Model)
# - GraduateStudent (Inherited Model)
# - Course (Container Model with enrollment logic)
# - Interactive CLI Menu with defensive error handling

class Student:
    def __init__(self, student_id, name, gpa=0.0):
        self.student_id = student_id
        self.name = name
        self.gpa = float(gpa)

    def is_honors(self):
        return self.gpa >= 3.5

    def __str__(self):
        honors_badge = " [Honors]" if self.is_honors() else ""
        return f"[{self.student_id}] {self.name} | GPA: {self.gpa:.2f}{honors_badge}"


class GraduateStudent(Student):
    def __init__(self, student_id, name, gpa, thesis_topic):
        super().__init__(student_id, name, gpa)
        self.thesis_topic = thesis_topic

    # Overridden honors: requires 3.8+ for graduate students
    def is_honors(self):
        return self.gpa >= 3.8

    def __str__(self):
        honors_badge = " [Grad Honors]" if self.is_honors() else ""
        return f"[{self.student_id}] (Grad) {self.name} | Thesis: '{self.thesis_topic}' | GPA: {self.gpa:.2f}{honors_badge}"


class Course:
    def __init__(self, course_code, title, max_capacity=3):
        self.course_code = course_code
        self.title = title
        self.max_capacity = int(max_capacity)
        self.roster = []  # List of Student / GraduateStudent objects

    def enroll(self, student):
        """
        Enrolls a student if capacity allows and student isn't already enrolled.
        Raises ValueError if course is full or student already in roster.
        """
        # Defensive Check 1: Already enrolled?
        for enrolled_student in self.roster:
            if enrolled_student.student_id == student.student_id:
                raise ValueError(f"Student {student.name} ({student.student_id}) is already enrolled in {self.course_code}.")

        # Defensive Check 2: Capacity check
        if len(self.roster) >= self.max_capacity:
            raise ValueError(f"Cannot enroll {student.name}. Course {self.course_code} is full (Max: {self.max_capacity}).")

        self.roster.append(student)
        print(f"Successfully enrolled {student.name} into {self.course_code}!")

    def display_roster(self):
        print(f"\n--- Roster for {self.course_code}: {self.title} ({len(self.roster)}/{self.max_capacity}) ---")
        if not self.roster:
            print("  (No students enrolled yet)")
        else:
            for i, student in enumerate(self.roster, 1):
                print(f"  {i}. {student}")

def main():
    course = Course("CSE110", "Principles of Programming", max_capacity=3)

    while True:
        print("\n=== SCAI Course Enrollment System ===")
        print("1. Enroll Undergrad Student")
        print("2. Enroll Graduate Student")
        print("3. Display Roster")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            # TODO: Implement Undergrad enrollment
            print("\n[Option 1: Undergrad enrollment selected]")
            try:
                student_id = (input("Enter your student ID: "))

                if not student_id:
                    raise ValueError("Please enter your student ID again, cannot be empty.")
                student_name = str(input("Enter your name: "))

                if not student_name :
                    raise ValueError("Name must not be empty")
                    
                student_gpa = float(input("Enter your GPA: "))

                if not student_gpa:
                    raise ValueError("Enter a GPA. i.e. 1.0, 2.5, etc.")
                elif student_gpa < 0.0:
                    raise ValueError("GPA cannot be negative.")
                elif student_gpa > 4.5:
                    raise ValueError("GPA cannot be over 4.5")
                
            except TypeError as e:
                print(f"\nEnrollment unsuccessful: {e}")
            

        elif choice == "2":
            # TODO: Implement Graduate enrollment
            print("\n[Option 2: Graduate enrollment selected]")
        elif choice == "3":
            course.display_roster()
        elif choice == "4":
            print("\nExiting system. Good luck at SCAI!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()