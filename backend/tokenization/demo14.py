n = int(input("Enter number of entries: "))
students = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    students[key] = value
print(students)