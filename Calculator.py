fn = float (input("Enter your first number:"))
sign = str(input("Enter your sign of arithmetic:"))
sn = float(input("Enter your second number:"))
if(sign=='+'):
    sum=fn+sn
    print("The Summation of",fn,"and",sn,"is",sum)
elif(sign == '-'):
    sub = fn-sn
    print("The Substraction of",fn,"and",sn,"is",sub)
elif(sign=='*'):
    mul = fn*sn
    print("The Multiplication of",fn,"and",sn,"is",mul)
elif(sign=='/'):
    div = fn/sn
    print("The Divisin of",fn,"and",sn,"is",div)
else:
    print("You have inputted an invalid sign")
    print("Try again")




