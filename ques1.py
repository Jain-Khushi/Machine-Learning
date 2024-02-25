num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

ch = input("Enter the operation you want to perform(+,-,*,/,**) : ")
result = 0
if ch=='+':
    result = num1 + num2
elif ch=='-':
    result = num1 - num2
elif ch=='*':
    result = num1 * num2
elif ch=='/':
    result = num1 / num2
elif ch=='**':
    result = num1 ** num2
else :
    print("Input character is not recogised!")

print(num1,ch,num2," : ",result)