# 성적 계산 프로그램

def mean(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if len(self.students) == 0:
            return 0
        total = sum(s.average() for s in self.students)
        return total / len(self.students)

def main():
    alice = Student("Alice", [90, 85, 92])
    bob = Student("Bob", [70, 75, 68])

    gb = GradeBook()
    gb.add_student(alice)
    gb.add_student(bob)

    print("전체 반 평균 점수:", round(gb.class_average(), 2))

    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

if __name__ == "__main__":
    main()