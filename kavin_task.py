import json
# The gobal variable to store the data getting from the user
student ={}

#Core function
def register_student(student_id, name, batch):
    #check the user_id to avoid the duplicate
    if student_id in student:
        print ("Student_id alredy exists!..")
        return 
    #alocated the parameter to the key value pare 
    student[student_id] = {
        "name": name,
        "batch": batch,
        "attendance":{
            "total_days":0,
            "present_days":0
        },
        "terms":{}
    }
    print("Student registered successfully.")

def add_term_result(student_id, term_name, subject_marks_dict):
    if student_id not in student:
        print("Student not found..!")
        # if we don'treturn the value none will appear
        return
    student[student_id]["terms"][term_name] = subject_marks_dict
    print("Term result added.")

def update_subject_mark(student_id, term, subject, new_mark):

    student[student_id]["terms"][term][subject] = new_mark
    print("Mark Added..")

def record_attendance(student_id, present_days, total_days):

    if student_id not in student:
        print("Student not found..!")
        return
    student[student_id]["attendance"]["total_days"] = total_days
    student[student_id]["attendance"]["present_days"] = present_days

    print("Attendance Added..")

def calculate_average(student_id):

    if student_id not in student:
        return 0
    #To find the average  we need to divide the sum total mark and total subject
    total = 0
    count = 0
    
    for term in student[student_id]["terms"].values():

        total += sum(term.values())
        count += len(term)

    if count == 0:
        return 0
    
    else:
        return round(total/count,2)
    
def calculate_attendance_percentage(student_id):
    
    att = student[student_id]["attendance"]
    #To get the attendance we need to divide the total and present days and multiple by 100 
    if att["total_days"] == 0 :
        return 0
    else:
        return round((att["present_days"] / att["total_days"]) * 100, 2)

def get_topper_by_term(term):

    topper = None
    higavg = 0

    #To take the key value pare seprately and check
    for sid , data in student.items():

        #To find the average for the term 

        if term in data ["terms"]:
            mark = data["terms"][term].values()
            avg = sum(mark)/len(mark)
        #To know the highest avg by compare with new avg all time and get the name
            if avg > higavg :
                higavg = avg
                topper = data["name"]

    #After finding the topper we place the name in the print statement  with round of avg
    if topper:
        print("Top Performer:", topper, "in", term, "with", round(higavg, 2), "average")
    else:
        print("No data for this term.")

#used gpt
def rank_students_by_overall_average(batch):

    ranking = []

    for sid, data in student.items():
        if data["batch"] == batch :
            avg = calculate_average(sid)
            ranking.append((avg, data["name"]))
    
    ranking.sort(reverse=True)
    #arrange the output by a order
    i = 1
    for item in ranking:
        name = item[0]
        avg = item[1]
        print(str(i) + ". " + name + " - " + str(avg))
        i += 1

def generate_student_report(student_id):
    
    #TO find the user id is in the student dict
    if student_id not in student:
        print("Student not found.")
        return
    
    #saving student is in a vareiable to make the code less complicated
    data = student[student_id]

    #first 3 can easly print
    print(f"\nStudent Report: {data['name']} ({student_id})")
    print("Batch:", data["batch"])
    print("Attendance:", calculate_attendance_percentage(student_id), "%")

    #there can be one and more terms in a student. so we can loop the term and  average to print all the terms
    for term, subjects in data["terms"].items():
        avg = round(sum(subjects.values()) / len(subjects), 2)
        print(f"{term} Average:", avg)

    #topper and overall average 
    print("Overall Average:", calculate_average(student_id))

def export_data_to_json(filename):
    #using the write in file handling we export the data to a new file
    with open(filename, "w") as f:
        json.dump(student, f, indent=4)
    print("Data exported successfully.")


def import_data_from_json(filename):
    #using the read in file handling we import the data to a new file
    #If i don't give the gobal key word the python think it as new variable
    global student
    with open(filename, "r") as f:
        student = json.load(f)
    print("Data imported successfully.")



#User Input Menu -------------------------------------------------------------------------------------------------------------------------------------------------

while True:

    print("1.Register Student")
    print("2.Add Term Result")
    print("3.Update Subject Mark")
    print("4.Record Attendance")
    print("5.Generate Student Report")
    print("6.Get Topper By Term")
    print("7.Rank Students By Batch")
    print("8.Export Data")
    print("9.Import Data")
    print("10.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        batch = input("Batch: ")
        register_student(sid, name, batch)

    elif choice == "2":
        sid = input("Student ID: ")
        term = input("Term Name: ")
        n = int(input("Number of subjects: "))
        subjects = {}

        for _ in range(n):
            sub = input("Subject: ")
            mark = int(input("Mark: "))
            subjects[sub] = mark

        add_term_result(sid, term, subjects)

    elif choice == "3":
        sid = input("Student ID: ")
        term = input("Term: ")
        subject = input("Subject: ")
        new_mark = int(input("New Mark: "))
        update_subject_mark(sid, term, subject, new_mark)

    elif choice == "4":
        sid = input("Student ID: ")
        present = int(input("Present Days: "))
        total = int(input("Total Days: "))
        record_attendance(sid, present, total)

    elif choice == "5":
        sid = input("Student ID: ")
        generate_student_report(sid)

    elif choice == "6":
        term = input("Enter Term Name: ")
        get_topper_by_term(term)

    elif choice == "7":
        batch = input("Enter Batch: ")
        rank_students_by_overall_average(batch)

    elif choice == "8":
        filename = input("Enter filename (example: data.json): ")
        export_data_to_json(filename)

    elif choice == "9":
        filename = input("Enter filename to import: ")
        import_data_from_json(filename)

    elif choice == "10":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")