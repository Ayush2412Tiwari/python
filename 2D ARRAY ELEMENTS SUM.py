#SUM OF ALL ELEMNETS OF 2D ARRAY
ilist_o_list=[[1,2,3],[4,5,6],[7,8,9],[10,11,12,13,14,15]]
sum=0
for x in ilist_o_list:
    for y in x:
        sum+=y
print(sum)
