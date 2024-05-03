# Student-Performance-Analysis

# Guide: Dataset Creation to Grade Calculation

## 1. Dataset Creation:

### Purpose:
Generate a dataset containing student information and marks for various subjects.

### Steps:
1. Define the structure of the dataset, including fields such as Name, USN, and marks for each subject.
2. Choose a method to generate student data, such as using random values or predefined data.
3. Ensure that the marks for each subject adhere to the specified criteria:
   - ISA1 and ISA2 marks should be out of 40 each.
   - ESA marks should be out of 100.
   - Assignments marks should be out of 20.

## 2. Read Dataset from CSV:

### Purpose:
Read the generated dataset from a CSV file for further processing.

### Steps:
1. Store the generated dataset in a CSV file named "student_dataset.csv" for easy access.
2. Use Python's `csv` module to read the dataset from the CSV file into memory.
3. Ensure that the dataset is properly parsed and stored in a suitable data structure for further analysis.

## 3. Grade Calculation Function:

### Purpose:
Define a function to calculate the percentage and grade for a given set of marks for a subject.

### Steps:
1. Define a function that takes the marks for a subject as input.
2. Convert ISA1 and ISA2 marks to out of 15 each, ESA marks to out of 50, and keep Assignments as is (out of 20).
3. Calculate the total marks obtained and the overall possible marks for the subject.
4. Calculate the percentage based on the obtained marks and possible marks.
5. Assign a grade based on the percentage obtained, following a predefined grading scale.

## 4. Calculate Subject Grades:

### Purpose:
Iterate through each student's data in the dataset and calculate the subject-wise grades.

### Steps:
1. Iterate through each student's data in the dataset.
2. For each student, iterate through each subject and calculate the percentage and grade using the previously defined function.
3. Display the subject-wise percentage and grade for each student.
4. Optionally, aggregate the data to calculate overall performance metrics such as average percentage or grade distribution across subjects.
