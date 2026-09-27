import streamlit as st
import numpy as np

st.title("STUDENT MARKS ANALYZER")

n = st.number_input(
    "Enter number of students : ",
    min_value=1,
    step=1
)

students_marks = []

for i in range(1, n + 1):
    marks = st.number_input(
        f"Enter marks for Student {i} : ",
        min_value=0,
        max_value=100,
        step=1,
        key=f"marks_{i}"
    )
    students_marks.append(marks)

if st.button("Analyze Marks"):

    marks_array = np.array(students_marks)

    st.header("Student Marks")
    st.write(marks_array)

    st.header("Array Information")

    st.write("Number of Dimensions :", marks_array.ndim)
    st.write("Number of Elements :", marks_array.size)
    st.write("Shape :", marks_array.shape)
    st.write("Data Type :", marks_array.dtype)

    st.header("Indexing")

    st.write("First Student Marks :", marks_array[0])
    st.write("Last Student Marks :", marks_array[n - 1])

    if n >= 3:
        st.write("Third Student Marks :", marks_array[2])

    st.header("Slicing")

    st.write("First Three Students :", marks_array[0:3])

    if n >= 3:
        st.write("Last Three Students :", marks_array[n - 3:n])

    st.header("Marks Analysis")

    total_marks = 0

    for i in range(len(marks_array)):
        total_marks += marks_array[i]

    total_elements = len(marks_array)

    st.write("Total Marks :", total_marks)
    st.write("Average Marks :", total_marks / total_elements)
    st.write("Highest Marks :", np.max(marks_array))
    st.write("Lowest Marks :", np.min(marks_array))