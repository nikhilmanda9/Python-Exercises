"""
In this program, we create a grade book of students and their scores and rank them
based on the number of points the student has obtained. 

The top three ranked students each earn a cash prize and the students that earn at least
950 points receive complementary remarks.

"""




def readGradebook():
    """
    This function reads a student name along with their grades. 
    
    Once, we read the student name and test score, we store this information into a dictionary.
    
    Then we return the grade book.
    """
    
    #Ask the user to enter the number of students
    numStudents = int(input("Enter the number of students: "))
          
    classGradebook = {} #create an empty dictionary to store student name and scores
    
    #Validates to see if the user enters at least 3 for the number of students
    if numStudents < 3:
        print("Please enter a minimum of three students")
        quit()
    
    #for each student, we create a grade book of scores
    for student in range(0, numStudents):
        studentName = input("Enter the student's name: ")
        studentScore = int(input("Enter the student's grade: "))
        
        classGradebook[studentName] = studentScore #assign the user entered grade to the student
        student += 1
    
    return classGradebook




def ranktopStudents(classGradebook):
    """
    This function ranks the top 3 students based on the highest grades.
    
    We accept the classGradebook parameter which has the student's names and their grades. 
    
    Then, once we sort their grades from the highest score to the lowest score, 
    then we return a sorted grade book.
    
    The highest scoring student earns $110, the second highest scoring student earns $100,
    and the third highest scoring student earns $90
    
    """
    
    #we sort the students with their scores in descending order
    sortedGradebook = sorted(classGradebook.items(), key = lambda item: item[1], reverse = True)
    
    print("The student with the first rank is {}, who has scored {} points and earns a cash prize of $110.".format(sortedGradebook[0][0], sortedGradebook[0][1]))
    print("The student with the second rank is {}, who has scored {} points and earns a cash prize of $100.".format(sortedGradebook[1][0], sortedGradebook[1][1]))
    print("The student with the third rank is {}, who has scored {} points and earns a cash prize of $90.".format(sortedGradebook[2][0], sortedGradebook[2][1]))
   
    return sortedGradebook
    

  

def studentAppreciation(sortedGradebook):
    """
    This function accepts the sortedGradebook parameter that contains the top 3 ranked students
    first and provides appreciation to the students who scored at least 950 points. 
    """
    for grade in sortedGradebook:
        #checks if the student grade is at least 950 points
        if grade[1] >= 950:
            print("Excellent job {} for scoring {} points.".format(grade[0], grade[1]))
        else:
            break
    
    
    
 
#This is the main execution of the program.
   
classGrades = readGradebook()  #call the readGradebook() function and store the result in classGrades
print()

#call the ranktopStudents function by passing in classGrades and store the result in rankStudents
rankStudents = ranktopStudents(classGrades)
print()

#call the studentAppreciation function by passing in the sorted grade book 
studentAppreciation(rankStudents)


        