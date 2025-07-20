"""
Jessie Miers
CSD325 
7/19/2025

This program imports the json to read the student.json file.
Displays original list, then allows uses to add a new student,
and displays updated list, after which the json file is appended 
a message to the user indicating this has happened.

"""

import json
#Loads the original students from JSON file.
def load_students(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
#Display information for each student.    
def print_students(students, header):
    print(f"\n{header}")
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

#Prompts users to input new student information.
def add_student():
    print("\nAdd new student information:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    student_id = input("Student ID:")
    email  = input("Email:")
    return{
        "F_Name": first_name,
        "L_Name": last_name,
        "Student_ID": student_id,
        "Email": email

    }
#Saves the updated student inputs to the JSON file using json.dump.
def save_students(filename, students):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)

def main():
    filename =  'student.json'
    students = load_students(filename)

    #Displays original Student List.
    print_students(students, "Original Student List")

    
    #Gets user inputs for Added Student.
    new_student = add_student()

    #Appends json file.
    students.append(new_student)
    
    #Displays updated list
    print_students(students, "Updated Student List")

    #Saves the updated list and displays message file has been saved.
    save_students(filename, students)
    print("\nstudent.json file has been updated.")

if __name__ == "__main__":
    main()