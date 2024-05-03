import csv

def calculate_grade(subject_marks):
    total_marks = 0
    total_possible_marks = 0

    # Converting ISA marks to out of 15
    isa1_percent = subject_marks['ISA1'] * (15 / 40)
    isa2_percent = subject_marks['ISA2'] * (15 / 40)
    # Converting ESA marks to out of 50
    esa_percent = subject_marks['ESA'] * (50 / 100)
    # Assignments are already out of 20
    assignment_percent = subject_marks['Assignments']

    # Calculating total marks for the subject
    subject_total = isa1_percent + isa2_percent + esa_percent + assignment_percent
    total_marks += subject_total
    total_possible_marks += 15 + 15 + 50 + 20  # Maximum marks for each subject

    # Calculating percentage
    percentage = (subject_total / total_possible_marks) * 100

    # Assigning grade based on percentage
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'

    return percentage, grade

def calculate_subject_grades(usn):
    with open('student_datasett.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for student in reader:
            if student['USN'] == usn:
                print(f"Subject Grades for {student['Name']} (USN: {student['USN']}):")
                for subject in ['Maths', 'Physics', 'Chemistry', 'Biology', 'English']:
                    marks = {
                        'ISA1': int(student[f"{subject} (ISA1)"]),
                        'ISA2': int(student[f"{subject} (ISA2)"]),
                        'ESA': int(student[f"{subject} (ESA)"]),
                        'Assignments': int(student[f"{subject} (Assignments)"])
                    }
                    percentage, grade = calculate_grade(marks)
                    print(f"{subject}: Percentage = {percentage:.2f}%, Grade = {grade}")
                return
        print("Student not found in the dataset.")

# Prompting the user to input the USN
usn = input("Enter the USN of the student: ")
calculate_subject_grades(usn)
