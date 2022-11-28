# CODE FOR FIBONAACI USING FOR LOOP
count=20
i=0
j=1
print("1:",i)
print("2:",j)
for x in range(3,count+1):
    print(x,":",i+j)
    i,j=j,i+j
