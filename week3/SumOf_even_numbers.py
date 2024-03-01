sum=0
count_3=0
count_5=0
num=[]
for i in range(1,50):
    if i%2==0:
        if i%3==0:
            count_3+=1
            num.append("Three")
        elif i%5==0:
            count_5+=1
            num.append("Five")
        else:
         sum+=i
         num.append(i)
print(num)
print(f"\nTotal sum of even number except 3 and 5 is: {sum}")
print(f"Number of times 3 replaced is {count_3}")
print(f"Number of times 5 replaced is {count_5}")
