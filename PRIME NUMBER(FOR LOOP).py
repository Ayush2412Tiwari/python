#CODE FOR PRIME NUMBER USING FOR LOOP
num=int(input("enter number"))
for x in range(2,num):
    if num%x==0:
        print("not a prime number")
        break
else:
    print(num,":is a prime number")
