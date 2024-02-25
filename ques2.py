num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("Operations : 1)OR  2)AND  3)Check for equality  4)NOT  5)XOR")
op = input("Enter the operation you want to perform : ")
result = 0
if op=='OR':
    result = num1 or num2
elif op=='AND':
    result = num1 and num2
elif op=='Check for equality':
    result = num1 == num2
elif op=='NOT':
    result = not num1
elif op=='XOR':
    result = num1 ^ num2
else :
    print("Input character is not recogised!")

print(num1,op,num2," : ",result)