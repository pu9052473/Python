# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# example:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# output: 56.00

n = int(input("n:"))
student_marks = {}
for _ in range(n):
    name, *line = input("pair of name:[marks] :-").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("q:")
print(student_marks[query_name])
total = sum(student_marks[query_name])
print(total)
average = total / len(student_marks[query_name])
print(format(average, '.2f'))



