import csv
import random

def generate_dataset(num_students):
    subjects = ['Maths', 'Physics', 'Chemistry', 'Biology', 'English']
    dataset = []

    for i in range(num_students):
        student = {}
        student['Name'] = f"Student {i+1}"
        student['USN'] = f"USN{i+1:04d}"
        student['Subjects'] = {}

        for subject in subjects:
            marks = {
                'ISA1': random.randint(0, 40),
                'ISA2': random.randint(0, 40),
                'ESA': random.randint(0, 100),
                'Assignments': random.randint(0, 20)
            }
            student['Subjects'][subject] = marks

        dataset.append(student)

    return dataset

def save_dataset_to_csv(dataset, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'USN', 'Maths (ISA1)', 'Maths (ISA2)', 'Maths (ESA)', 'Maths (Assignments)',
                         'Physics (ISA1)', 'Physics (ISA2)', 'Physics (ESA)', 'Physics (Assignments)',
                         'Chemistry (ISA1)', 'Chemistry (ISA2)', 'Chemistry (ESA)', 'Chemistry (Assignments)',
                         'Biology (ISA1)', 'Biology (ISA2)', 'Biology (ESA)', 'Biology (Assignments)',
                         'English (ISA1)', 'English (ISA2)', 'English (ESA)', 'English (Assignments)'])
        for student in dataset:
            row = [student['Name'], student['USN']]
            for subject, marks in student['Subjects'].items():
                row.extend([marks['ISA1'], marks['ISA2'], marks['ESA'], marks['Assignments']])
            writer.writerow(row)

# Generating dataset for 10 students
num_students = 10
dataset = generate_dataset(num_students)

# Saving dataset to CSV
save_dataset_to_csv(dataset, 'student_dataset.csv')
print("Dataset saved successfully as 'student_dataset.csv'")















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
