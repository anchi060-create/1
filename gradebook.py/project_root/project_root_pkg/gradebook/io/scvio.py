import csv
from ..models import Student

def load_students_from_csv(path):
    students = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            scores = [float(x) for x in row[1:]]
            students.append(Student(name, scores))
    return students

def save_students_to_csv(path, students):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for s in students:
            writer.writerow([s.name] + s.scores)