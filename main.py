# main.py - Simple console version

from student_module import *

def main():
    print("\n" + "="*50)
    print("BRIGHTMIND TUITION CENTRE SYSTEM")
    print("="*50)
    
    students_list = []
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Register Student")
        print("2. Calculate Fees")
        print("3. Display Student Info")
        print("4. Show All Students")
        print("5. Data Analysis")
        print("6. Exit")
        
        choice = input("Choose option (1-6): ")
        
        # Exception handling for invalid input
        try:
            if choice == "1":
                student = register_student()
                students_list.append(student)
                print(f"\n✓ Student {student.name} registered successfully!")
                
            elif choice == "2":
                if students_list:
                    print("\nSelect student:")
                    for i, s in enumerate(students_list):
                        print(f"{i+1}. {s.name}")
                    idx = int(input("Enter number: ")) - 1
                    if 0 <= idx < len(students_list):
                        calculate_fee(students_list[idx])
                    else:
                        print("Invalid selection!")
                else:
                    print("No students registered yet!")
                    
            elif choice == "3":
                if students_list:
                    print("\nSelect student:")
                    for i, s in enumerate(students_list):
                        print(f"{i+1}. {s.name}")
                    idx = int(input("Enter number: ")) - 1
                    if 0 <= idx < len(students_list):
                        display_student_information(students_list[idx])
                    else:
                        print("Invalid selection!")
                else:
                    print("No students registered yet!")
                    
            elif choice == "4":
                if students_list:
                    print("\n--- ALL STUDENTS ---")
                    for student in students_list:
                        print(f"- {student.name} (Reg: {student.reg_no})")
                else:
                    print("No students yet.")
                    
            elif choice == "5":
                analyze_students(students_list)
                
            elif choice == "6":
                print("\nThank you for using BrightMind System!")
                break
                
            else:
                print("Invalid option. Choose 1-6.")
                
        except ValueError:
            print("Error: Please enter a valid number!")
        except Exception as e:
            print(f"An error occurred: {e}")

# Demonstrate operator overloading and magic methods
def demo_features():
    print("\n" + "="*50)
    print("DEMONSTRATING OOP FEATURES")
    print("="*50)
    
    # Create two students for demo
    s1 = Student("John Doe", "REG001", "010101-01-1234", "Form 4")
    s2 = Student("Jane Smith", "REG002", "020202-02-5678", "Form 5")
    
    s1.add_subject("Math", 150)
    s1.add_subject("Science", 140)
    s2.add_subject("English", 130)
    
    # Magic method __str__
    print("\n__str__ method demo:")
    print(str(s1))
    print(str(s2))
    
    # Operator overloading __add__
    print("\n__add__ operator overloading demo:")
    total = s1 + s2
    print(f"Total fees for {s1.name} and {s2.name}: RM {total:.2f}")

if __name__ == "__main__":
    demo_features()
    main()