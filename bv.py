#function to get info of student
def get_student_info():
    student_Id = input("Enter the sudent_id: ")
    name = input("Enter the  Name: ")
    batch = int(input("Enter the Batch Year: "))

    return student_Id,name,batch
#function to get info of student attendance
def get_attendance_info():
    total_days = int(input("Enter the Total Working days: "))
    present_days = int(input("Enter the Total present days: "))

    if present_days > total_days:
        print("The present day is invalid..!,Check total days")

    return {
        "total_days": total_days,
        "present_days": present_days
    }

#function to get info of the student term and mark
def get_term_info():
    term_name = input("Enter the term: ")
    no_of_sub = int(input("Enter the total number of subject: "))
    #storing the data in dic
    marks = {}

    for i in range(no_of_sub):
        subject_name = input("Enter the subject name: ")
        mark = int(input("Enter the mark: "))
        marks[subject_name] = mark

    return term_name,marks
# calculate Term mark to get the average 
def caculate_avg_term(marks):
    total = sum(marks.values())
    avg = total/ len(marks)
    return avg

#function to get attendance average
def calculate_avg_attendance(attendance):
    att_avg = (attendance["present_days"]/attendance["total_days"])*100
    return att_avg

#-----------------------------------------------------------------------------------------------------

sudent_id,name,batch = get_student_info()
attendance = get_attendance_info()
term_name, marks = get_term_info()

students = {
    "student_id": sudent_id,
    "name" : name,
    "batch": batch,
    "attendance": attendance,
    "term":{
        "term_name":term_name,
        "marks":marks
    }
    
}

average = caculate_avg_term(students["term"]["marks"])
attendance_percentage = calculate_avg_attendance(students["attendance"])


students["attendance"]["att_avg"] = round(attendance_percentage, 2)
students["term"]["average"] = round(average, 2)

print(f"""
Student ID : {students["student_id"]}
Name       : {students["name"]}
Batch      : {students["batch"]}

Attendance % : {students["attendance"]["att_avg"]}

Term      : {students["term"]["term_name"]}
Marks     : {students["term"]["marks"]}
Average   : {students["term"]["average"]}
""")
