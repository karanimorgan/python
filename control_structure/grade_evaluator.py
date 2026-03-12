def evaluate_grade():
    score = int (input ("enter the score (0-100):"))
    # "F" if score is between 90, and 100, print "A"
    # if score is between 80, and 89, print "B"
    # if score is between 70, and 79, print"c"print
    # if score is Between 60, and 69, print "D"
    # if score is below 60, print
    if score >= 90 and score <=100:
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score>= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    elif score < 60:
        print("F")
    else:
        print("Invalid score. Please enter score between 0 and 100")
if __name__ == "__main__":
    evaluate_grade()
