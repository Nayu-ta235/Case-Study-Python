# student_module.py - Simple version for average students

class Student:
    """Base class for Student"""
    
    def __init__(self, name, reg_no, ic_number, grade_level):
        self.name = name
        self.reg_no = reg_no
        self.ic_number = ic_number
        self.grade_level = grade_level
        self.subjects = []
        self.fees = []
    
    def __str__(self):
        return f"Student Name: {self.name} | Reg No: {self.reg_no}"
    
    def __add__(self, other):
        # Operator overloading - add total fees of two students
        return self.calculate_total_fee() + other.calculate_total_fee()
    
    def add_subject(self, subject, fee):
        self.subjects.append(subject)
        self.fees.append(fee)
    
    def calculate_total_fee(self):
        return sum(self.fees)
    
    def display_info(self):
        print("\n" + "="*40)
        print("STUDENT INFORMATION")
        print("="*40)
        print(f"Name: {self.name}")
        print(f"Registration No: {self.reg_no}")
        print(f"IC Number: {self.ic_number}")
        print(f"Grade Level: {self.grade_level}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Total Fee: RM {self.calculate_total_fee():.2f}")
        print("="*40)


class PremiumStudent(Student):
    """Subclass with inheritance"""
    
    def __init__(self, name, reg_no, ic_number, grade_level, discount=10):
        # Function overloading using default parameter
        super().__init__(name, reg_no, ic_number, grade_level)
        self.discount = discount
    
    def __str__(self):
        return f"PREMIUM: {self.name} | {self.discount}% discount"
    
    def calculate_total_fee(self):
        original = sum(self.fees)
        discount_amount = original * self.discount / 100
        return original - discount_amount
    
    def display_info(self):
        print("\n" + "="*40)
        print("PREMIUM STUDENT INFORMATION")
        print("="*40)
        print(f"Name: {self.name}")
        print(f"Registration No: {self.reg_no}")
        print(f"IC Number: {self.ic_number}")
        print(f"Grade Level: {self.grade_level}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Original Fee: RM {sum(self.fees):.2f}")
        print(f"Discount: {self.discount}%")
        print(f"Final Fee: RM {self.calculate_total_fee():.2f}")
        print("="*40)


# FUNCTION 1: Register student
def register_student():
    print("\n--- STUDENT REGISTRATION ---")
    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")
    ic_number = input("Enter IC number: ")
    grade_level = input("Enter grade level (e.g., Form 1-5): ")
    
    premium_choice = input("Premium member? (y/n): ").lower()
    
    if premium_choice == 'y':
        student = PremiumStudent(name, reg_no, ic_number, grade_level)
    else:
        student = Student(name, reg_no, ic_number, grade_level)
    
    return student


# FUNCTION 2: Calculate fee
def calculate_fee(student):
    print("\n--- SUBJECT REGISTRATION ---")
    print("Available subjects and fees:")
    print("1. Mathematics - RM150")
    print("2. Science - RM140")
    print("3. English - RM130")
    print("4. Bahasa Malaysia - RM120")
    print("5. History - RM110")
    
    subjects_fees = {
        "1": ("Mathematics", 150),
        "2": ("Science", 140),
        "3": ("English", 130),
        "4": ("Bahasa Malaysia", 120),
        "5": ("History", 110)
    }
    
    while True:
        choice = input("\nSelect subject (1-5) or 'done' to finish: ")
        
        if choice.lower() == 'done':
            break
        elif choice in subjects_fees:
            subject, fee = subjects_fees[choice]
            student.add_subject(subject, fee)
            print(f"Added: {subject} - RM{fee}")
        else:
            print("Invalid choice. Try again.")
    
    total = student.calculate_total_fee()
    print(f"\nTotal fee: RM {total:.2f}")
    return total


# FUNCTION 3: Display student information
def display_student_information(student):
    student.display_info()


# Matrix processing function
def analyze_students(students_list):
    """Simple data analysis using lists (no NumPy/Pandas needed)"""
    if not students_list:
        print("No students to analyze.")
        return
    
    print("\n" + "="*50)
    print("STUDENT DATA ANALYSIS")
    print("="*50)
    
    # Simple analysis using lists
    print("\nAll Students:")
    for i, student in enumerate(students_list, 1):
        print(f"{i}. {student.name} - RM {student.calculate_total_fee():.2f}")
    
    # Calculate average fee
    total_fees = [s.calculate_total_fee() for s in students_list]
    average_fee = sum(total_fees) / len(total_fees)
    print(f"\nAverage Fee: RM {average_fee:.2f}")
    print(f"Highest Fee: RM {max(total_fees):.2f}")
    print(f"Lowest Fee: RM {min(total_fees):.2f}")
    
    # Filter students with fee > RM100
    print("\nStudents with fee > RM100:")
    for student in students_list:
        if student.calculate_total_fee() > 100:
            print(f"- {student.name}: RM {student.calculate_total_fee():.2f}")