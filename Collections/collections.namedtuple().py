from collections import namedtuple

numOfStudents=int(input())
Students = namedtuple("student", input().split())
print(sum(
    [int(Students(*(input().split())).MARKS) for n in range(numOfStudents)])/numOfStudents)
 
