number_remainder=0
number_quitent=0
def digit(number,number_remainder):
    for i in range(len(str(number))):
        number_remainder+=number%10
        number=number//10
    return number_remainder

number=int(input("Entere the digit: "))
digit_1=digit(number,number_remainder)
print("The sum of {} is: {}".format(number,digit_1))

