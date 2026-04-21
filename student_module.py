import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student Class
class Student:
    def __init__(self, name, reg_no, ic, grade):
        self.name = name
        self.reg_no = reg_no
        self.ic = ic
        self.grade = grade
        self.subjects = []
        self.fees = []
    
    def __str__(self):
        return f"Name: {self.name}, Reg: {self.reg_no}"
    
    def __add__(self, other):
        return sum(self.fees) + sum(other.fees)
    
    def add_subject(self, subject, fee):
        self.subjects.append(subject)
        self.fees.append(fee)
    
    def total_fee(self):
        return sum(self.fees)
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Reg No: {self.reg_no}")
        print(f"IC: {self.ic}")
        print(f"Grade: {self.grade}")
        print(f"Subjects: {self.subjects}")
        print(f"Total Fee: RM{self.total_fee()}")

# PremiumStudent subclass with inheritance
class PremiumStudent(Student):
    def __init__(self, name, reg_no, ic, grade, discount=10):
        super().__init__(name, reg_no, ic, grade)
        self.discount = discount
    
    def __str__(self):
        return f"Premium: {self.name}, {self.discount}% off"
    
    def total_fee(self):
        original = sum(self.fees)
        return original - (original * self.discount / 100)
    
    def display(self):
        print(f"Premium Student: {self.name}")
        print(f"Reg No: {self.reg_no}")
        print(f"Discount: {self.discount}%")
        print(f"Subjects: {self.subjects}")
        print(f"Final Fee: RM{self.total_fee()}")

# FUNCTION 1: Register student
def register_student():
    print("\n=== REGISTER STUDENT ===")
    name = input("Enter name: ")
    reg_no = input("Enter registration number: ")
    ic = input("Enter IC number: ")
    grade = input("Enter grade: ")
    
    ans = input("Premium student? (y/n): ")
    if ans == 'y':
        return PremiumStudent(name, reg_no, ic, grade)
    else:
        return Student(name, reg_no, ic, grade)

# FUNCTION 2: Calculate fee
def calculate_fee(student):
    print("\n=== SUBJECTS AND FEES ===")
    print("1. Math = RM100")
    print("2. Science = RM90")
    print("3. English = RM80")
    
    while True:
        choice = input("Choose subject (1-3) or 'done': ")
        if choice == 'done':
            break
        elif choice == '1':
            student.add_subject("Math", 100)
            print("Added Math - RM100")
        elif choice == '2':
            student.add_subject("Science", 90)
            print("Added Science - RM90")
        elif choice == '3':
            student.add_subject("English", 80)
            print("Added English - RM80")
        else:
            print("Wrong choice")
    
    print(f"\nTotal fee: RM{student.total_fee()}")

# FUNCTION 3: Display student information
def display_student_info(student):
    print("\n=== STUDENT INFO ===")
    student.display()

# Matrix processing using NumPy and Pandas
def matrix_processing(students):
    print("\n=== MATRIX PROCESSING ===")
    
    # Create array/dataframe
    data = []
    for s in students:
        data.append([s.name, s.total_fee()])
    
    df = pd.DataFrame(data, columns=['Name', 'Fee'])
    print("DataFrame:")
    print(df)
    
    # Display array attributes
    print(f"\nShape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
    # Indexing and slicing
    print(f"\nFirst row:\n{df.iloc[0]}")
    
    # Mathematical analysis
    fees = df['Fee'].values
    print(f"\nMean fee: RM{np.mean(fees):.2f}")
    print(f"Max fee: RM{np.max(fees):.2f}")
    print(f"Min fee: RM{np.min(fees):.2f}")
    
    # Filter data
    high_fees = df[df['Fee'] > 100]
    print(f"\nStudents with fee > RM100:\n{high_fees}")
    
    # Sort data
    sorted_df = df.sort_values('Fee', ascending=False)
    print(f"\nSorted by fee:\n{sorted_df}")
    
    # Graph using Matplotlib
    plt.bar(df['Name'], df['Fee'])
    plt.title('Student Fees')
    plt.xlabel('Student')
    plt.ylabel('Fee (RM)')
    plt.show()