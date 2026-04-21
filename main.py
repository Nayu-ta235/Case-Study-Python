import student_module as sm

def main():
    print("="*40)
    print("BRIGHTMIND TUITION CENTRE")
    print("="*40)
    
    students_list = []
    
    while True:
        print("\n1. Register Student")
        print("2. Calculate Fee")
        print("3. Display Student Info")
        print("4. Matrix Processing")
        print("5. Exit")
        
        # Exception handling
        try:
            choice = int(input("Choose (1-5): "))
            
            if choice == 1:
                s = sm.register_student()
                students_list.append(s)
                print(f"{s.name} registered!")
                
            elif choice == 2:
                if len(students_list) > 0:
                    print("\nSelect student:")
                    for i, stu in enumerate(students_list):
                        print(f"{i+1}. {stu.name}")
                    idx = int(input("Enter number: ")) - 1
                    sm.calculate_fee(students_list[idx])
                else:
                    print("No students yet!")
                    
            elif choice == 3:
                if len(students_list) > 0:
                    print("\nSelect student:")
                    for i, stu in enumerate(students_list):
                        print(f"{i+1}. {stu.name}")
                    idx = int(input("Enter number: ")) - 1
                    sm.display_student_info(students_list[idx])
                else:
                    print("No students yet!")
                    
            elif choice == 4:
                if len(students_list) > 0:
                    sm.matrix_processing(students_list)
                else:
                    print("No students to analyze!")
                    
            elif choice == 5:
                print("Goodbye!")
                break
                
            else:
                print("Choose 1-5 only!")
                
        except ValueError:
            print("Error: Please enter a number!")
        except Exception as e:
            print(f"Error: {e}")

# Demonstrate magic methods and operator overloading
print("\n=== DEMO MAGIC METHODS ===")
s1 = sm.Student("Ali", "R001", "123", "Form4")
s2 = sm.Student("Abu", "R002", "456", "Form5")
s1.add_subject("Math", 100)
s2.add_subject("Science", 90)

print("__str__ demo:")
print(str(s1))
print(str(s2))

print("\n__add__ demo (operator overloading):")
total = s1 + s2
print(f"Total fees both students: RM{total}")

if __name__ == "__main__":
    main()