word = str(input("Enter Word: ")).lower()
vow = ("a","e",'i','o','u')
for i in word:
    if i in vow:
        print(i,end="")