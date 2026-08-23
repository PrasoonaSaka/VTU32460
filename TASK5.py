N = int(input("Enter number of students: "))
students = []
for i in range(N):
    name, marks = input("Enter name and marks: ").split()
    students.append((name, int(marks)))
K = int(input("Enter K: "))
students = sorted(students, key=lambda x: (-x[1], x[0]))
print(" ".join(name for name, marks in students[:K]))
