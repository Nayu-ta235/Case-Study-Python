# student_module.py
# Contains Student class and functions

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
        return f"""
        Name: {self.name}
        Reg No: {self.reg_no}
        IC: {self.ic}
        Grade: {self.grade}
        Subjects: {', '.join(self.subjects)}
        Total Fee: RM{self.total_fee()}
        """

# PremiumStudent with inheritance
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
        return f"""
        PREMIUM STUDENT
        Name: {self.name}
        Reg No: {self.reg_no}
        IC: {self.ic}
        Grade: {self.grade}
        Subjects: {', '.join(self.subjects)}
        Discount: {self.discount}%
        Original Fee: RM{sum(self.fees)}
        Final Fee: RM{self.total_fee()}
        """

# FUNCTION 1: Register student
def register_student(name, reg_no, ic, grade, is_premium):
    if is_premium:
        return PremiumStudent(name, reg_no, ic, grade)
    else:
        return Student(name, reg_no, ic, grade)

# FUNCTION 2: Calculate fee
def calculate_fee(student, selected_subjects):
    subjects_fees = {
        "Mathematics": 100,
        "Science": 90,
        "English": 80,
        "Bahasa Malaysia": 70,
        "History": 60
    }
    
    for subject in selected_subjects:
        student.add_subject(subject, subjects_fees[subject])
    
    return student.total_fee()

# FUNCTION 3: Display student info
def display_student_info(student):
    return student.display()

# Matrix processing with NumPy and Pandas - UPDATED to return figure
def matrix_processing(students_list):
    if len(students_list) == 0:
        return None, None
    
    # Create DataFrame
    data = []
    for s in students_list:
        data.append({
            'Name': s.name,
            'Reg No': s.reg_no,
            'Grade': s.grade,
            'Total Fee': s.total_fee(),
            'Type': 'Premium' if isinstance(s, PremiumStudent) else 'Regular'
        })
    
    df = pd.DataFrame(data)
    
    # Display array attributes (printed to console)
    print("="*50)
    print("MATRIX PROCESSING OUTPUT")
    print("="*50)
    print(f"DataFrame Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    # Indexing and slicing
    print(f"\nFirst 2 rows:")
    print(df.head(2))
    
    # Mathematical analysis
    fees_array = df['Total Fee'].values
    print(f"\nMathematical Analysis:")
    print(f"Mean Fee: RM{np.mean(fees_array):.2f}")
    print(f"Max Fee: RM{np.max(fees_array):.2f}")
    print(f"Min Fee: RM{np.min(fees_array):.2f}")
    print(f"Standard Deviation: RM{np.std(fees_array):.2f}")
    
    # Filter data
    high_fees = df[df['Total Fee'] > 100]
    print(f"\nStudents with fee > RM100:")
    print(high_fees if not high_fees.empty else "None")
    
    # Sort data
    sorted_df = df.sort_values('Total Fee', ascending=False)
    print(f"\nSorted by fee (highest first):")
    print(sorted_df)
    print("="*50)
    
    # Create graph - RETURN the figure instead of showing
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df['Name'], df['Total Fee'], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    ax.set_title('Student Fees Report - BrightMind Tuition Centre', fontsize=14, fontweight='bold')
    ax.set_xlabel('Student Name', fontsize=12)
    ax.set_ylabel('Fee (RM)', fontsize=12)
    ax.set_ylim(0, max(df['Total Fee']) + 50)
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'RM{height:.0f}', ha='center', va='bottom', fontsize=10)
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    return df, fig