a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operation=input("add/sub/mul/div/mod:")
if(operation=="add"):
	print(a+b)
elif(operation=="sub"):
	print(a-b)
elif(operation=="mul"):
	print(a*b)
elif(operation=="div"):
    print(a/b)
elif(operation=="mod"):
	print(a%b)
else:
    print("invalid operation")
