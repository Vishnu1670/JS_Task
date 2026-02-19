import json

students = {}
# Getting student data
def register_student():
    student_id = input("Enter the Roll_Number: ")
    name = input("Enter the name: ")
    batch = input("Enter the year: ")

    students[student_id]= {
        "name": name,
        "batch": batch,
        "attendan":{
            "total_days":0,
            "present_days":0
        },
        "terms" : {}                    
    }
    return("Register Successfully")
# getting the attendance datail and calculating the average
def attendance_reg():
    print("Enter the student_id to add the attendance..")
    student_id = input("Enter the student_Id: ")
    # check the id is in the register
    if student_id not in students:
        return("Student_id not found..!")
        
    # getting the value for the attendance
    total_day = int(input("Enter the total no of days: "))
    present_day = int(input("Enter the total no of days present: "))

    # moving to the student dict
    students[student_id]["attendan"]["total_days"] =  total_day
    students[student_id]["attendan"]["present_days"] =  present_day

    # calculating the attendance average
    avg_att = students[student_id]["attendan"]
    #total days is 0 the avg can be 0
    if avg_att["total_days"] == 0:
        return 0
    #if the present days is greater than total days it's don't make sense
    elif avg_att["present_days"] > avg_att ["total_days"]:
        return "Enter the correct value of the present days"
    #using formula to get the average data
    else:
        avg=(avg_att["present_days"]/avg_att["total_days"])*100
        print("Average of attendance: ",round(avg,2))
        

#Getting the term mark details
def add_term():
    student_id = input("Enter the sudent_id:")
    if student_id in students:

        term_name = input("Enter the Term name: ")
        n = int(input("How many Subjects: "))

        subject = {}

        for i in range(n):
            sub_name = input("Enter the subject name: ")
            mark = int(input("Enter the mark: "))
            subject[sub_name] = mark
        students[student_id]["terms"][term_name] = subject
        print("Term added successfully!")
        avg = sum(subject.values()) / len(subject)
        print("Average for", term_name, ":", round(avg, 2))
 
#---------------------------------------------------------------------------------------------------------------------------------------------------
#loop for repit the function
while True:

    print("\n1. Register Student")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        print(register_student())
        print(attendance_reg())
        print(add_term())

    elif choice == "2":
        print("\nFinal Student Data:")
        print(json.dumps(students, indent=4))
        break

    else:
        print("Invalid choice! Try again.")