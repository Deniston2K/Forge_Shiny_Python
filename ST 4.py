num=[]

n=int(input("Enter the number of inputs: "))
x=1
while x<n+1:
    num.append(int(input("Enter numbers {}: ".format(x))))
    x+=1
print(min(num))

