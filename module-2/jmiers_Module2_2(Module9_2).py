"""
Jessie Miers
CSD 205
5/11/2025

This program is designed to use methods from Student class to calculate
the GPA from the user inputs for credit hours and letter grades, It converts
the letter grades to a numerical value and displays cumulative GPA along with 
student from user inputs for first and last name. 

Uses numerical equivalent for grades from table displayed here:
https://myrun.newark.rutgers.edu/how-calculate-your-cumulative-gpa#:~:text=Add%20up%20your%20grade%20points.,you%20took%2C%20which%20is%2012.&text=Therefore%2C%203.5%20would%20be%20your%20GPA.

This program was a difficult in the beginning, I had to work out so many errors base
poor stucture within my main fuction calling back to my methods within the Student class.
Though I think I have flushed out an effective program with good validation checks. 

"""
class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_credits = 0
        self.total_grade_points = 0 

    def add_course(self, credits, grade):

        numerical_grade = self.numerical_grade_conversion(grade)

        #Adds credits per grade input

        self.total_credits += credits

        #Calculates total of grade points by multipling grade points by credits 

        self.total_grade_points += numerical_grade * credits
  
    def numerical_grade_conversion(self,grade):
        grade = grade.strip().upper()

        #Numerical equivalent dictionary based off Rutgers University-Newark 

        numerical_equivalent = {'A':4.0,'B+':3.5,'B':3,'C+':2.5,'C':2,'D':1,'F':0.0}

        return numerical_equivalent.get(grade)

    def calculate_gpa(self):
        #Calculates GPA from total grade points and total credits 
        if self.total_credits == 0:
            return 0.0
      

        return self.total_grade_points / self.total_credits

    def display_gpa(self):

        gpa = self.calculate_gpa()

        print(f"\nStudent: {self.first_name.title()} {self.last_name.title()}\n\nCumulative GPA:\t{gpa:.2f}\n")   
        
    
def main():

    #Prompt user for first and last name

    first_name = input("\nEnter student's first name:\t")

    last_name = input("\nEnter student's last name:\t")
    
    student = Student( first_name,last_name)
    
    while True:

        try:
            #Prompt user for number of credit hours

            credits = int(input("\nEnter credit hours:\t"))

            if credits <= 0:
                #Error checks for negative numbers and zero inputs

                print("\nInvalid Input. Please input non-zero positive numbers.")
                continue

        except ValueError:

            #Error displayed if non-numeric is input 

            print("\nInvalid Input. Please input a valid number.")

            continue  

        
        while True:
        
            grade = input("\nEnter Grade Letter('A','B+','B','C+','C','D','F'):\t")
            #Validates user input for grade is in the numerical grade conversion method

            if student.numerical_grade_conversion(grade) is None:

                #Error message displayed if invalid or grade not present numberical_grade_conversion

                print("\nInvalid Letter Grade. Please only use 'A','B+','B','C+','C','D','F'")
                continue

            
            break

        student.add_course(credits,grade)            
                
        while True:
                    #Prompts user to if they would like to add course or not

                    reply = input("\nAdd another course? (Y/N):\t").strip().upper()

                    #If input is 'Y' loops back to credit input
                    if reply == 'Y':   
                        break
                    
                    
                    #If input is 'N' displays cumulative GPA and closes program
                    elif reply == 'N':
                
                        student.display_gpa()

                        return

                    #If input is not 'Y' or 'N' this error message is displayed

                    else:
                        
                        print("\nPlease only input 'Y' or 'N'")
                        


       

    
  

main()