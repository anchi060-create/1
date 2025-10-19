def mean(scores) :
    if len(scores) == 0 :
        return 0
    return sum(scores) / len(scores)

def letter_grade(score) :
    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    else:
        return "F"