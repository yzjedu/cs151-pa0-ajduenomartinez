# Programmers:  Antonio Dueno
# Course:  CS151, Zelalem Yalew
# Due Date: 9/18/2024
# Programming Assignment: 1
# Problem Statement: This program is designed to calculate the minimum amount of hours
# recommended to study on an assignment.
# Data In: Difficulty of assignment, Urgency of assignment, Type of assignment
# Data Out:  Minimum recommended amount of time to study in hours.
# Credits: Zybook homework assignment 01, and the website below explaining the "elif" command:
# https://www.w3schools.com/python/gloss_python_elif.asp

#This is the text that prints asking and explaining the program to the user.
print("Hello! In this program you will enter the urgency of an assignment, the difficulty of an assignment, "
       "and the type of assignment. \nFor this program to work, you must enter urgency on a scale of 1-5 and difficulty "
      "on a scale of 1-5. \nFor the type of assignment, you must enter 1 for a homework, 2 for a reading, "
      "3 for a project, and 4 for an exam.")

#this is the prompt for inputting urgency of assignment
urgency_of_assignment=float(input("Please enter urgency of assignment:"))
if urgency_of_assignment==1:
    urgency_of_assignment=0.5
if urgency_of_assignment==2:
    urgency_of_assignment=1.0
if urgency_of_assignment==3:
    urgency_of_assignment=1.5
if urgency_of_assignment==4:
    urgency_of_assignment=2.0
if urgency_of_assignment==5:
    urgency_of_assignment=2.5
if urgency_of_assignment>5:
    print("error: assignment urgency over 5")

#this is the prompt for inputting difficulty of assignment
difficulty_of_assignment=float(input("Please enter difficulty of assignment:"))
if difficulty_of_assignment>5:
    print("error: assignment difficulty over 5")

#this is the prompt for inputting the type of assignment
type_of_assignment=float(input("Please enter type of assignment:"))
if type_of_assignment==1:
    type_of_assignment=5
if type_of_assignment==2:
    type_of_assignment=6.5
if type_of_assignment==3:
    type_of_assignment=8.5
if type_of_assignment==4:
    type_of_assignment=10
if type_of_assignment>10:
    print("error: assignment type over 4")

#this is the calculation for the recommended amount of time for studying.
recommended_time=((type_of_assignment+urgency_of_assignment)*difficulty_of_assignment)/24



if recommended_time >= 2.5:
    print("The minimum recommended amount of time you should spend on your assignment is two and a half hours.")
elif recommended_time >= 2:
    print("The minimum recommended amount of time you should spend on your assignment is two hours.")
elif recommended_time >= 1.5:
    print("The minimum recommended amount of time you should spend on your assignment is an hour and a half.")
elif recommended_time >= 1:
    print("The minimum recommended amount of time you should spend on your assignment is an hour.")
elif recommended_time >= 0.5:
    print("The minimum recommended amount of time you should spend on your assignment is thirty minutes.")
elif recommended_time < 0.5:
    print("The minimum recommended amount of time you should spend on your assignment is less than thirty minutes.")










