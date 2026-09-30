import streamlit as st

st.title("STUDENT GRADE MANAGEMENT SYSTEM")

n = st.number_input(
    "Enter number of students : ",
    min_value=1,
    max_value=100,
    step=1
)

student = []

for i in range(1, n + 1):
    st.subheader(f"Student {i}")

    students_detail = {
        "name": st.text_input(f"Enter student name : ", key=f"name_{i}"),
        "marks": st.number_input(
            f"Enter marks : ",
            min_value=0,
            max_value=100,
            step=1,
            key=f"marks_{i}"
        )
    }

    student.append(students_detail)

if st.button("Calculate Grades"):

    st.header("STUDENT RESULTS")

    for students_detail in student:

        student_name = students_detail["name"]
        student_marks = students_detail["marks"]

        st.write("Student Name :", student_name)
        st.write("Student Marks :", student_marks)

        if student_marks > 90:
            grade = "A+"

        elif student_marks > 85:
            grade = "A"

        elif student_marks > 80:
            grade = "B+"

        elif student_marks > 75:
            grade = "B"

        elif student_marks > 60:
            grade = "C"

        else:
            grade = "Fail"

        st.write("Grade :", grade)
        st.write("---")