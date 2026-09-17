#Name: Samuel Benitez
#Period: PM
#Student Performance Analyzer

#program intro
print("========================================")
print("       STUDENT PERFORMANCE ANALYZER")
print("========================================")
print()
print("Enter student's information below")
print()
print()

#student info gather
sName = input("What is the student's name? : ")
print()
sGradeL = input("What grade level is the student in? : ")
print()
sAavg = input("What is the student's assignment average? : ")
print()
sQavg = input("What is the student's quiz average? : ")
print()
sTavg = input("What is the student's test average? : ")
print()
sAttendance = input("What is the student's attendance percentage? : ")
print()
sMissing = input("How many missing assignments does student have? : ")
print()

#calculate grade func
def calculate_grade(aAvg, qAvg, tAvg):
    decA = int(aAvg) * 0.01
    decQ = int(qAvg) * 0.01
    decT = int(tAvg) * 0.01

    weightedA = decA * 0.3
    weightedQ = decQ * 0.3
    weightedT = decT * 0.4

    overall = (weightedA + weightedQ + weightedT) * 100
    return overall

overall_grade = calculate_grade(sAavg, sQavg, sTavg)
print()
print(f"Student's Overall: {overall_grade:.2f}")
print()

#letter grade