students={
    "name":"Arif",
    "department":"cs",
    "batch":12,
    "roll_no":232433,
    "gpa":3.3,
}
print(students)

#accessing element
print(students["name"])
print(students["department"])

#adding a new item
students["section"]="b"
print(students)
students["supervisor"]="Moiz"
students["city"]="islamabad"
students["university"]="Air"
print(students["department"])
print(students)
print(students["university"])

#updating the the previous elements 
students["city"]="pindi"
print(students)
students["department"]="cyber"
print(students)

#removing item using pop()
students.pop("batch")
students.pop("department")
students.pop("gpa")
print(students)

#removing last element
students.popitem()
print(students)
students.popitem()
print(students)

#getting all keys
print(students.keys())
print(students.values())
print(students.items())

#clearing the dictionary
students.clear()
print(students)
