#CODE FOR PRIME NUMBER USING WHILE LOOP
num=int(input("enter number"))
x=2
while x<num:
    if num%x==0:
        print(num,'is not prime number')
        break
    x+=1
else:
    print(num,'is a prime number')
