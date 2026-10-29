students = [
    {"name": "Aarav", "math": 85, "python": 92, "statistics": 78},
    {"name": "Priya", "math": 91, "python": 88, "statistics": 95},
    {"name": "Rahul", "math": 67, "python": 74, "statistics": 69},
    {"name": "Sneha", "math": 95, "python": 96, "statistics": 93},
    {"name": "Karan", "math": 72, "python": 65, "statistics": 70}
]
for i in students:
    total_score = i["math"] + i["python"] + i["statistics"]
    average_score = total_score / 3
    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    else:
        grade = "D"
    i["total_score"] = total_score
    i["average_score"] = average_score
    i["grade"] = grade
search=input("Enter the name of the student to search for: ")
for i in students:
    if i["name"].lower() == search.lower():
        print("Student found!")
        print("Name:", i["name"])
        print("Math score:", i["math"])
        print("Python score:", i["python"])
        print("Statistics score:", i["statistics"])
        print("Total score:", i["total_score"])
        print("Average score:", i["average_score"])
        print("Grade:", i["grade"])
        break
ranking = sorted(students, key=lambda x: x["total_score"], reverse=True)
for i in ranking:
    print(i["name"], ":", i["total_score"])