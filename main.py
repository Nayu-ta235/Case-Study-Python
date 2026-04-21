# main.py
# Main program with Streamlit GUI

import streamlit as st
import pandas as pd
from student_module import register_student, calculate_fee, display_student_information, analyze_student_data, Student, PremiumStudent

# Subject dictionary with fees
SUBJECTS = {
    "Mathematics": 150.00,
    "Science": 140.00,
    "English": 130.00,
    "Bahasa Malaysia": 120.00,
    "History": 110.00,
    "Physics": 160.00,
    "Chemistry": 160.00,
    "Biology": 155.00
}

def main():
    """Main program with Streamlit GUI"""
    
    st.set_page_config(page_title="BrightMind Tuition Centre", page_icon="📚", layout="wide")
    
    # Title and header
    st.title("📚 BrightMind Tuition Centre Management System")
    st.markdown("---")
    
    # Initialize session state
    if 'student' not in st.session_state:
        st.session_state.student = None
    if 'students_list' not in st.session_state:
        st.session_state.students_list = []
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Student Registration")
        
        # Input fields
        name = st.text_input("Full Name", placeholder="Enter student's full name")
        reg_no = st.text_input("Registration Number", placeholder="e.g., BMT2024001")
        ic_number = st.text_input("IC Number", placeholder="e.g., 050101-01-1234")
        grade_level = st.selectbox("Grade Level", ["Form 1", "Form 2", "Form 3", "Form 4", "Form 5"])
        is_premium = st.checkbox("Premium Membership (10% discount)")
        
        # Subject selection
        st.subheader("📖 Subject Selection")
        selected_subjects = st.multiselect(
            "Choose subjects",
            list(SUBJECTS.keys()),
            help="Select one or more subjects"
        )
        
        # Display subject fees
        if selected_subjects:
            st.write("**Selected Subjects and Fees:**")
            subject_fee_data = []
            total = 0
            for subject in selected_subjects:
                fee = SUBJECTS[subject]
                subject_fee_data.append({"Subject": subject, "Fee (RM)": fee})
                total += fee
            
            df_fees = pd.DataFrame(subject_fee_data)
            st.dataframe(df_fees, use_container_width=True)
            st.info(f"💰 **Subtotal: RM {total:.2f}**")
            
            if is_premium:
                discount = total * 0.10
                final_total = total - discount
                st.success(f"✨ **Premium Discount (10%): -RM {discount:.2f}**")
                st.success(f"🎯 **Total after discount: RM {final_total:.2f}**")
        else:
            st.warning("Please select at least one subject")
        
        # Register button
        if st.button("✅ Register Student", type="primary", use_container_width=True):
            try:
                # Exception handling for input validation
                if not name:
                    st.error("❌ Name cannot be empty!")
                elif not reg_no:
                    st.error("❌ Registration number cannot be empty!")
                elif not ic_number:
                    st.error("❌ IC number cannot be empty!")
                elif not selected_subjects:
                    st.error("❌ Please select at least one subject!")
                else:
                    # Register student
                    student = register_student(name, reg_no, ic_number, grade_level, is_premium)
                    
                    if student:
                        # Calculate fees
                        subjects_with_fees = {subj: SUBJECTS[subj] for subj in selected_subjects}
                        total_fee, subjects, fees = calculate_fee(student, subjects_with_fees)
                        
                        if total_fee is not None:
                            st.session_state.student = student
                            st.session_state.students_list.append(student)
                            st.success(f"✅ Student {name} registered successfully!")
                            st.balloons()
                    else:
                        st.error("Registration failed!")
                        
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    
    with col2:
        st.subheader("👨‍🎓 Student Information")
        
        if st.session_state.student:
            try:
                # Display student information
                student_info = display_student_information(st.session_state.student)
                if student_info:
                    st.code(student_info, language="text")
                
                # Demonstrate operator overloading
                if len(st.session_state.students_list) >= 2:
                    st.subheader("➕ Operator Overloading Demo")
                    s1 = st.session_state.students_list[0]
                    s2 = st.session_state.students_list[1]
                    total_fees_both = s1 + s2
                    st.info(f"Total fees for {s1.name} and {s2.name}: RM {total_fees_both:.2f}")
                
                # Demonstrate magic methods
                st.subheader("✨ Magic Methods Demo")
                st.write(f"**__str__ method output:** {st.session_state.student}")
                
            except Exception as e:
                st.error(f"Error displaying student info: {str(e)}")
        else:
            st.info("No student registered yet. Please complete registration form.")
    
    # Data Analysis Section
    st.markdown("---")
    st.subheader("📊 Student Data Analysis")
    
    if st.button("📈 Perform Data Analysis", use_container_width=True):
        try:
            if len(st.session_state.students_list) > 0:
                with st.spinner("Analyzing data..."):
                    # Perform matrix processing and analysis
                    df = analyze_student_data(st.session_state.students_list)
                    
                    # Display DataFrame in Streamlit
                    st.subheader("Student DataFrame")
                    st.dataframe(df, use_container_width=True)
                    
                    st.success("Analysis completed successfully!")
            else:
                st.warning("No students to analyze. Please register at least one student.")
        except Exception as e:
            st.error(f"Analysis error: {str(e)}")
    
    # Display all registered students
    if st.session_state.students_list:
        st.subheader("📋 All Registered Students")
        student_data = []
        for s in st.session_state.students_list:
            student_data.append({
                "Name": s.name,
                "Reg No": s.reg_no,
                "Grade": s.grade_level,
                "Subjects": len(s.subjects),
                "Total Fee": f"RM {s.calculate_total_fee():.2f}",
                "Type": "Premium" if isinstance(s, PremiumStudent) else "Regular"
            })
        st.dataframe(pd.DataFrame(student_data), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("© 2025 BrightMind Tuition Centre Management System | Developed with ❤️ using Python")

if __name__ == "__main__":
    main()