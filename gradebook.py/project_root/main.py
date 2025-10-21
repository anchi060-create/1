from models import Student, GradeBook

def main() :
    alice = Student("Alice", [90, 85, 92])
    bob = Student("Bob", [70, 75, 68])
    
    gb = GradeBook()
    gb.add_student(alice)
    gb.add_student(bob)
    
    print("전체 반 평균 점수 : ", round(gb.class_average(), 2))
    
    for s in gb.students :
        print(f"{s.name} - 평균 : {s.average() :.1f}, 학점 : {s.grade()}")
        
        
if __name__ == "__main__" : 
    main()