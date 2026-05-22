'''Capgemini
1. Problem Statement - Raj wants to know the maximum marks scored by him in each semester.
The mark should be between 0 to 100, if it goes beyond the range display "You have entered
invalid mark.”
Sample Input 1:
· Enter no of semester: 3
· Enter no of subjects in 1 semester: 3
· Enter no of subjects in 2 semester: 4
· Enter no of subjects in 3 semester: 2
· Marks obtained in semester 1:
50
60
70
· Marks obtained in semester 2:
90
98
76
67
· Marks obtained in semester 3:
89
76
Sample Output 1:
. Maximum mark in 1 semester:70
. Maximum mark in 2 semester:98
. Maximum mark in 3 semester:89'''


if __name__=="__main__":
    sem=int(input("Enter number of Semester."))
    for i in range(sem):
        pass