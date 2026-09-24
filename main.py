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
sGradeL = int(input("What grade level is the student in? : "))
print()
sAavg = input("What is the student's assignment average? : ")
print()
sQavg = input("What is the student's quiz average? : ")
print()
sTavg = input("What is the student's test average? : ")
print()
sAttendance = float(input("What is the student's attendance percentage? : "))
print()
sMissing = int(input("How many missing assignments does student have? : "))
print()

#calculate grade func
def calculate_grade(aAvg, qAvg, tAvg):
    decA = float(aAvg) * 0.01
    decQ = float(qAvg) * 0.01
    decT = float(tAvg) * 0.01

    weightedA = decA * 0.3
    weightedQ = decQ * 0.3
    weightedT = decT * 0.4

    overall = (weightedA + weightedQ + weightedT) * 100
    return overall

overall_grade = calculate_grade(sAavg, sQavg, sTavg)
print()
print(f"Student's Overall: {overall_grade:.2f}")

#letter grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        letter = "A"
    elif overall_grade >= 80:
        letter = "B"
    elif overall_grade >= 70:
        letter = "C"
    elif overall_grade >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter
letterGrade = letter_grade(overall_grade)
print("Letter Grade: ", letterGrade)
print()

#attendance status
print()

def attendance_status(attendance):
    if attendance >= 95:
        status = "Excellent Attendance"
    elif attendance >= 90:
        status = "Good Attendance"
    elif attendance >= 80:
        status = "Attendance Warning"
    else:
        status = "Poor Attendance"
    return status
Astatus = attendance_status(sAttendance)
print("-Attendance Status-")
print(Astatus)
print()

#missing assignment status
print()

def assignment_status(missing_assignments):
    if missing_assignments == 0:
        status = "Excellent"
    elif missing_assignments <= 2:
        status = "Good"
    elif missing_assignments <= 4:
        status = "Warning"
    elif missing_assignments >= 5:
        status = "Critical"
    return status
MAstatus = assignment_status(sMissing)
print("-Missing Assignment Status-")
print(MAstatus)
print()

#academic eligibility
print()

def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Student passed all three req.")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")
    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")
check_eligibility(overall_grade, sAttendance, sMissing)
print()

#high honors
def checkHigh_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High Honors: NO")
            print("Reason: Attendance req. not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade req. not met.")
checkHigh_honors(overall_grade, sAttendance, sMissing)
print()
print()

#good standing
def checkGood_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        standing = "YES"
    else:
        standing = "NO"
    return standing
good_standing = checkGood_standing(overall_grade, sAttendance)
print("Good Standing: ", good_standing)
print()

#check support
def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")
check_support(overall_grade, sAttendance)
print()

#student login
iUser = input("Enter Username: ")
iPin = input("Enter PIN: ")

cUser = "student"
cPin = "1234"

if iUser == cUser:
    if iPin == cPin:
        print()
        print("Login Successfull!")
    else:
        print()
        print("Login Failed: Incorrect PIN")
else:
    print()
    print("Login Failed: Incorrect username")
print()

#grade level message
def gradeLevel_message(grade_level):
    if grade_level == 9:
        print("Welcome to your freshman year!")
    elif grade_level == 10:
        print("Keep building your skills!")
    elif grade_level == 11:
        print("Junior year -- keep pushing!")
    elif grade_level == 12:
        print("Senior year -- finish strong!")
    else:
        print("Invalid grade level.")
gradeLevel_message(sGradeL)
print()

#strongest academic category
def strongest_category(assignment_avg, quiz_avg, test_avg):
    if quiz_avg < assignment_avg > test_avg:
        print("Strongest Category: Assignments")
    elif test_avg < quiz_avg > assignment_avg:
        print("Strongest Category: Quizzes")
    elif quiz_avg < test_avg > assignment_avg:
        print("Strongest Category: Tests")
strongest_category(sAavg, sQavg, sTavg)
print()

#extra cred
def checkAdv_status(overall, att, missing):
    if overall >= 90 and att >= 95 or overall >= 85 and missing == 0:
        sStatus = "OUTSTANDING STUDENT"
    else:
        sStatus = "STANDARD STUDENT"
    return sStatus
studentStatus = checkAdv_status(overall_grade, sAttendance, sMissing)

#to round answered averages
fltSa = float(sAavg)
fltSq = float(sQavg)
fltSt = float(sTavg)

#final student summary
print("========================================")
print("             STUDENT SUMMARY             ")
print("========================================")
print("~Student~")
print(sName)
print("~Grade Level~")
print(sGradeL)
print("~Student Status~")
print(studentStatus)
print()
print()
print("Assignment Avg: ", round(fltSa, 2))
print("Quiz Avg: ", round(fltSq, 2))
print("Test Avg: ", round(fltSt, 2))
print()
print("~Overall Grade~")
print(round(overall_grade, 2))
print("~Attendance~")
print(sAttendance)
print()
gradeLevel_message(sGradeL)
print()
print("========================================")
