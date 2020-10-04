#Finding odd numbers form two given values

def odd(n,m):
    odd_num = []
    for x in range(n,m+1):
        if x%2!=0:
            odd_num.append(x)
    return odd_num

def even(n,m):
    even_num=[]
    for x in range(n,m+1):
        if x%2==0:
            even_num.append(x)
    return even_num
flag=True
while flag:
    n=int(input("Enter the start value: "))
    m=int(input("Enter the end value: "))
    user_input=input("Enter the required output odd or even: ")
    if user_input=="even":
        print(even(n,m))
        flag=False
    elif user_input=="odd":
        print(odd(n, m))
        flag=False
    else:
        print("Kindly enter odd or even")

#this code is correct-------------------------
# a=[10]
# b=[]
# print(a)
# a.append('10')
# b=a
# print(b)

#this code is wrong----------------------------
# a=[10]
# b=[]
# print(a)
# b=a.append('10')
# print(b)
# # print(a.append(5))

