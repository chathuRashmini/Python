# Print the average of the marks array for the student name provided, 
# showing 2 places after the decimal by using a dictionary which keeps 
# name and marks as key value pairs.
# ex:
# input->
# 2
# mark 10 20 30
# sonia 30 20 40
# mark

# output = 20.00 because marks average is that

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = list()
    marks = sum(student_marks.get(query_name, 0))
    result = marks/3
    print("{:.2f}".format(result))