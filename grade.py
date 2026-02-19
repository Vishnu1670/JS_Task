def get_grade(mark):

    if mark >=90 :
        print ("Your Grade is: A!")
    elif mark >=80 and mark <= 90:
        print ("Your Grade is: B!")
    elif mark >=70 and mark <= 80:
        print ("Your Grade is: C!")
    elif mark >=60 and mark <= 70:
        print ("Your Grade is: D!")
    elif mark >=50 and mark <= 60:
        print ("Your Grade is: E!")
    else:
        print("Fail..!")

get_grade(49)