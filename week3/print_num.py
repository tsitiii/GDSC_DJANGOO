for i in range(99):
    result="{:02d}".format(i)
    print(result,end=',')
print(99)

#or use this code
for i in range(100):

    result="{:02d}".format(i)
    print(result, end=',' if i!=99 else "\n")
