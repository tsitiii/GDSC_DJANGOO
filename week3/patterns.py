choice=input("Enter any charcter for your pattern: ")
choice2=int(input("On How many lines do u want it to be displayed? "))
for i in range(choice2):
    for j  in range(i+1):
        print(choice,end='')
    print()
