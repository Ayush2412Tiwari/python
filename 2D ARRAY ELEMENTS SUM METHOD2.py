#ALTERNATE
ilist_o_list=[[1,2,3],[4,5,6],[7,8,9],[10,11,12,13,14,15]]
sum=0
for i in range(0,len(ilist_o_list)):
    for j in range(0,len(ilist_o_list[i])):
        sum+=ilist_o_list[i][j]
    print(sum)
