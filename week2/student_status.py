stud_detail = {}
num = int(input("           *************WELCOME!!!*************\n\nEnter number of students you want manage: "))
def add():
    for i in range(num):
        stud_name = input("Enter name: ")
        stud_age = int(input("Enter age: "))
        stud_grade = float(input("Enter grade: "))
        stud_detail[stud_name] = {"Name": stud_name, "Age": stud_age, "Grade": stud_grade}
    return stud_detail

def display():
    for i in stud_detail:
        print(stud_detail[i])

def search():
    name=input("Enter name of student u want to search: ")
    found= False
    for i in stud_detail:
       if (i==name):
            print(stud_detail[i])
            found=True
    if not found :
            print("wrong student")
def update():
    nwname=input("Enter name of student u want to change: ")
    inputt=int(input("what do u want to update?\n1.name \n2.Age \n3.Grade: "))
    
    if(inputt==1):
        new_name=input("enter new name: ")
        if nwname in stud_detail:
                stud_detail[nwname]["Name"]=new_name
        else:
               print("Student not found!")
    elif (inputt==2):
        new_age=int(input("Enter the updated age: "))
        if nwname in stud_detail:
             stud_detail[nwname]["Age"]=new_age
        else:
             print("Student not found!")
    elif (inputt==3):
        new_grade=float(input("Enter the updated age: "))
        if nwname in stud_detail:
                stud_detail[nwname]["Grade"]=new_grade
        else:
               print("Student not found!")
def delete():
    unwanted=input("Enter the name of student u want to delet: ")
    if unwanted in stud_detail:
        del stud_detail[unwanted]

def choicee():
    while(True):
        choice=int(input("Enter Ur choice: "))
        if (choice==1):
            add()
        elif (choice==2):
            display()
        elif(choice==3):
            search()
        elif (choice==4):
            update()
        elif (choice==5):
            delete()
        elif (choice==6):
             break
        else:
            print("wrong choice! try again")
        yess=input("Do u want to continue? \"yes\" \"no\" ")
        if yess.lower()!="yes":
            break

print("1.Add student information\n2.Display \n3.Search \n4.Update \n5.Delete \n6.Exit")
choicee() 
