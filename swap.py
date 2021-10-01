def swaplist(l,pos1,pos2):
    n = len(l)    
    print(l) 
    # Swapping           
    #temp = l[pos1]
    #l[pos1] = l[pos2]
    #l[pos2] = temp
    l[pos1],l[pos2]=l[pos2],l[pos1]  
    return l      

l= [1, 2, 5, 9, 6, 12,90]
#pos1= 3
#pos2= 5
pos1,pos2=3,5

print(l)
print("Swapped list is : ",swaplist(l,pos1,pos2))