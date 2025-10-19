from untils import mean, letter_grade

class Student :
    def __init__(self, name, scores) :
        self.name = name
        self.scores = scores
        
    def average(self) :
        return mean(self.scores)

    def grade(self) :
        return letter_grade(self.average()) 
    
class GradeBook :
    def __init__(self) :
        self.students = []      
        
    def add_student(self, student) :
        self.students.append(student)
        
    def class_average(self) :
        total = 0
        for s in self.students :
            total += s.average()
        return total / len(self.students)