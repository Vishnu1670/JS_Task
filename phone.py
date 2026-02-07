user_in = str(input("Enter Number: "))
count = 1 #the start of count 
for i in range(9000000000,9100000001): #the number range
    if user_in in str(i) : #in str only it can check through the word by word
        print(count,i) #9,valu
        if count == 10:
            break
        count+=1