#using for loop----------------------
m=int(input("Enter the start value:"))
n=int(input("Enter the start value:"))
sum=0
count=0
for x in range(m,n+1):
    sum+=x
    count+=1
print("Average {}".format(sum/count))

#using While loop---------------------
sum_1=0
count_1=0
while n>m-1:
    sum_1+=n
    count_1+=1
    n-=1
print("Average {}".format(sum_1/count_1))


