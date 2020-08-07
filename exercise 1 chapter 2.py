# number_one= int(input("please enter number 1: "))
# number_two=int(input("please enter number 2: "))
# number_three=int(input("please enter number 3: "))
# average=number_one + number_two + number_three
# print(f"Average is {average//3}")
num1,num2,num3 = input("enter three numbers ").split(",")
average=int(num1)+int(num2)+int(num3)
print(f"average is {average//3}")