import streamlit as st
import pandas as pd
from student_module import *

# Page setup
st.set_page_config(page_title="BrightMind Tuition Centre", layout="wide")

st.title("📚 BrightMind Tuition Centre Management System")
st.markdown("---")

# Session state to store students
if 'students' not in st.session_state:
    st.session_state.students = []
if 'current_student' not in st.session_state:
    st.session_state.current_student = None

# Subject list with fees
SUBJECTS = {
    "Mathematics": 100,
    "Science": 90,
    "English": 80,
    "Bahasa Malaysia": 70,
    "History": 60
}

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Student Registration")
    
    # Input fields
    name = st.text_input("Full Name")
    reg_no = st.text_input("Registration Number")
    ic = st.text_input("IC Number")
    grade = st.selectbox("Grade Level", ["Form 1", "Form 2", "Form 3", "Form 4", "Form 5"])
    is_premium = st.checkbox("Premium Student (10% discount)")
    
    # Subject selection
    st.subheader("📖 Select Subjects")
    selected_subjects = st.multiselect("Choose subjects", list(SUBJECTS.keys()))
    
    # Show fees for selected subjects
    if selected_subjects:
        st.write("**Selected Subjects and Fees:**")
        total = 0
        for subj in selected_subjects:
            fee = SUBJECTS[subj]
            st.write(f"- {subj}: RM{fee}")
            total += fee
        
        st.info(f"**Subtotal: RM{total}**")
        
        if is_premium:
            discount = total * 0.1
            final = total - discount
            st.success(f"After 10% discount: RM{final}")
    
    # Register button with exception handling
    if st.button("Register Student", type="primary"):
        try:
            # Exception handling for empty inputs
            if not name:
                st.error("❌ Name cannot be empty!")
            elif not reg_no:
                st.error("❌ Registration number cannot be empty!")
            elif not ic:
                st.error("❌ IC number cannot be empty!")
            elif not selected_subjects:
                st.error("❌ Please select at least one subject!")
            else:
                # Register student
                student = register_student(name, reg_no, ic, grade, is_premium)
                
                # Calculate fees
                total_fee = calculate_fee(student, selected_subjects)
                
                # Add to list
                st.session_state.students.append(student)
                st.session_state.current_student = student
                
                st.success(f"✅ {name} registered successfully!")
                st.balloons()
                
        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    st.subheader("👨‍🎓 Student Information")
    
    if st.session_state.current_student:
        # Display student info
        info = display_student_info(st.session_state.current_student)
        st.code(info, language="text")
        
        # Show operator overloading demo if at least 2 students
        if len(st.session_state.students) >= 2:
            st.subheader("➕ Operator Overloading Demo")
            s1 = st.session_state.students[0]
            s2 = st.session_state.students[1]
            total_both = s1 + s2
            st.info(f"Total fees for {s1.name} and {s2.name}: RM{total_both}")
        
        # Show magic method demo
        st.subheader("✨ Magic Method Demo")
        st.write(f"**__str__ output:** {st.session_state.current_student}")
    else:
        st.info("No student registered yet. Fill the form on the left.")

# Show all registered students
st.markdown("---")
st.subheader("📋 All Registered Students")

if st.session_state.students:
    data = []
    for s in st.session_state.students:
        data.append({
            "Name": s.name,
            "Reg No": s.reg_no,
            "Grade": s.grade,
            "Subjects": len(s.subjects),
            "Total Fee": f"RM{s.total_fee()}",
            "Type": "Premium" if isinstance(s, PremiumStudent) else "Regular"
        })
    st.dataframe(pd.DataFrame(data), use_container_width=True)
else:
    st.warning("No students registered yet.")

# Matrix Processing and Data Analysis
st.markdown("---")
st.subheader("📊 Student Data Analysis (NumPy & Pandas)")

if st.button("Run Data Analysis"):
    try:
        if len(st.session_state.students) > 0:
            with st.spinner("Analyzing data..."):
                # This will print to console and show graph
                df, plot = matrix_processing(st.session_state.students)
                
                # Display DataFrame in Streamlit
                st.subheader("Student DataFrame")
                st.dataframe(df, use_container_width=True)
                
                st.subheader("Analysis Results")
                st.write(f"- Total students: {len(st.session_state.students)}")
                st.write(f"- Average fee: RM{df['Total Fee'].mean():.2f}")
                st.write(f"- Highest fee: RM{df['Total Fee'].max():.2f}")
                st.write(f"- Lowest fee: RM{df['Total Fee'].min():.2f}")
                
                st.success("Analysis completed! Check the graph window that opened.")
        else:
            st.error("No students to analyze. Please register at least one student.")
    except Exception as e:
        st.error(f"Analysis error: {e}")

# Footer
st.markdown("---")
st.markdown("© 2025 BrightMind Tuition Centre")