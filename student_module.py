# student_module.py
# Contains Student class, PremiumStudent subclass, and related functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Student:
    """Base class for Student"""
    
    def __init__(self, name, reg_no, ic_number, grade_level):
        """Magic method __init__ for object initialization"""
        self.name = name
        self.reg_no = reg_no
        self.ic_number = ic_number
        self.grade_level = grade_level
        self.subjects = []
        self.fees = []
        
    def __str__(self):
        """Magic method __str__ for string representation"""
        return f"Student: {self.name} (Reg: {self.reg_no}) - Grade {self.grade_level}"
    
    def __add__(self, other):
        """Magic method __add__ for operator overloading (total fees between two students)"""
        if isinstance(other, Student):
            total_fee1 = sum(self.fees)
            total_fee2 = sum(other.fees)
            return total_fee1 + total_fee2
        return NotImplemented
    
    def add_subject(self, subject_name, fee):
        """Method to add subject with fee"""
        self.subjects.append(subject_name)
        self.fees.append(fee)
    
    def calculate_total_fee(self):
        """Calculate total fee for the student"""
        return sum(self.fees)
    
    def display_info(self):
        """Display student information"""
        info = f"""
        {'='*40}
        STUDENT INFORMATION
        {'='*40}
        Name: {self.name}
        Registration No: {self.reg_no}
        IC Number: {self.ic_number}
        Grade Level: {self.grade_level}
        Subjects Enrolled: {', '.join(self.subjects) if self.subjects else 'None'}
        Total Fee: RM {self.calculate_total_fee():.2f}
        {'='*40}
        """
        return info


class PremiumStudent(Student):
    """Subclass PremiumStudent inheriting from Student"""
    
    def __init__(self, name, reg_no, ic_number, grade_level, discount_percentage=10):
        """Constructor with default parameter (function overloading concept)"""
        super().__init__(name, reg_no, ic_number, grade_level)
        self.discount_percentage = discount_percentage
    
    def __str__(self):
        """Override __str__ for PremiumStudent"""
        return f"Premium Student: {self.name} (Reg: {self.reg_no}) - {self.discount_percentage}% discount"
    
    def calculate_total_fee(self):
        """Override method to apply discount"""
        original_fee = sum(self.fees)
        discount_amount = original_fee * (self.discount_percentage / 100)
        final_fee = original_fee - discount_amount
        return final_fee
    
    def display_info(self):
        """Override display_info to show premium benefits"""
        info = f"""
        {'='*40}
        PREMIUM STUDENT INFORMATION
        {'='*40}
        Name: {self.name}
        Registration No: {self.reg_no}
        IC Number: {self.ic_number}
        Grade Level: {self.grade_level}
        Membership: PREMIUM
        Discount: {self.discount_percentage}%
        Subjects Enrolled: {', '.join(self.subjects) if self.subjects else 'None'}
        Original Total Fee: RM {sum(self.fees):.2f}
        Discount Amount: RM {(sum(self.fees) * self.discount_percentage/100):.2f}
        Final Total Fee: RM {self.calculate_total_fee():.2f}
        {'='*40}
        """
        return info


# Functions for the system
def register_student(name, reg_no, ic_number, grade_level, is_premium=False):
    """Function to register a new student"""
    try:
        if not name or not reg_no or not ic_number or not grade_level:
            raise ValueError("All fields are required!")
        
        if is_premium:
            student = PremiumStudent(name, reg_no, ic_number, grade_level)
        else:
            student = Student(name, reg_no, ic_number, grade_level)
        
        return student
    except ValueError as e:
        print(f"Registration Error: {e}")
        return None


def calculate_fee(student, subjects_with_fees):
    """Function to calculate fees for selected subjects"""
    try:
        if not student:
            raise ValueError("Invalid student object!")
        
        if not subjects_with_fees:
            raise ValueError("No subjects selected!")
        
        for subject, fee in subjects_with_fees.items():
            student.add_subject(subject, fee)
        
        total_fee = student.calculate_total_fee()
        return total_fee, student.subjects, student.fees
    except Exception as e:
        print(f"Fee Calculation Error: {e}")
        return None, None, None


def display_student_information(student):
    """Function to display student information"""
    try:
        if not student:
            raise ValueError("No student data to display!")
        
        return student.display_info()
    except Exception as e:
        print(f"Display Error: {e}")
        return None


def analyze_student_data(students_list):
    """Matrix processing and data analysis using NumPy and Pandas"""
    
    # Create DataFrame from student data
    data = []
    for student in students_list:
        data.append({
            'Name': student.name,
            'Registration No': student.reg_no,
            'Grade Level': student.grade_level,
            'Subjects Count': len(student.subjects),
            'Total Fee': student.calculate_total_fee(),
            'Student Type': 'Premium' if isinstance(student, PremiumStudent) else 'Regular'
        })
    
    # Create DataFrame using Pandas
    df = pd.DataFrame(data)
    
    # Display array/DataFrame attributes
    print("\n" + "="*60)
    print("MATRIX PROCESSING & DATA ANALYSIS")
    print("="*60)
    print("\n1. DataFrame created:")
    print(df)
    
    print("\n2. DataFrame Attributes:")
    print(f"   - Shape: {df.shape}")
    print(f"   - Columns: {list(df.columns)}")
    print(f"   - Data types:\n{df.dtypes}")
    
    # Indexing and slicing
    print("\n3. Indexing and Slicing:")
    print("   - First 2 rows:\n", df.head(2))
    print("   - Name and Total Fee columns:\n", df[['Name', 'Total Fee']])
    
    # Mathematical analysis using NumPy
    fees_array = df['Total Fee'].values
    print("\n4. Mathematical Analysis (NumPy):")
    print(f"   - Mean Fee: RM {np.mean(fees_array):.2f}")
    print(f"   - Median Fee: RM {np.median(fees_array):.2f}")
    print(f"   - Standard Deviation: RM {np.std(fees_array):.2f}")
    print(f"   - Min Fee: RM {np.min(fees_array):.2f}")
    print(f"   - Max Fee: RM {np.max(fees_array):.2f}")
    
    # Filter and sort data
    print("\n5. Filtered Data (Total Fee > RM 100):")
    filtered_df = df[df['Total Fee'] > 100]
    print(filtered_df if not filtered_df.empty else "   No students with fee > RM 100")
    
    print("\n6. Sorted Data (by Total Fee descending):")
    sorted_df = df.sort_values('Total Fee', ascending=False)
    print(sorted_df)
    
    # Create graph using Matplotlib
    plt.figure(figsize=(10, 6))
    
    # Bar chart for student fees
    names = df['Name']
    fees = df['Total Fee']
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    
    plt.bar(names, fees, color=colors[:len(names)])
    plt.xlabel('Student Name', fontsize=12)
    plt.ylabel('Total Fee (RM)', fontsize=12)
    plt.title('Student Fee Analysis - BrightMind Tuition Centre', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for i, (name, fee) in enumerate(zip(names, fees)):
        plt.text(i, fee + 5, f'RM{fee:.0f}', ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    return df