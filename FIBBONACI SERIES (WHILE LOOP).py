#CODE FOR FIBONACCI USING WHILE LOOP
limit=1000
i=1
j=1
count=2
print('1:',i)
print('2:',j)
while i+j<limit:
    count+=1
    print(count,':',i+j)
    i,j=j,i+j
