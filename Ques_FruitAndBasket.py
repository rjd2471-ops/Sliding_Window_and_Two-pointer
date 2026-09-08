#Ques Fruit Into Baskets.

fruits = [3,3,3,1,2,1,1,2,3,3,4]


max_count=0

for i in range(len(fruits)):
    
    my_set= set()
    
    for j in range(i,len(fruits)):
        
        my_set.add(fruits[j])
        
        if len(my_set)>2 :
           break
        max_count= max(max_count, j-i+1)
    
print(max_count)
#This is the brute force approch for this is and here time comp is O(NxN) and space comp is O(1).


#let's try the other approch for this is.____________________________________________________________________.

fruits = [3,1,3,1,3,3,3,2,3,3,4]

max_count=0
my_dict={}
i=0
for j in range(len(fruits)):
    my_dict[fruits[j]]= my_dict.get(fruits[j],0)+1
    
    if len(my_dict)>2:
        my_dict[fruits[i]]-=1
        
        if my_dict[fruits[i]]==0:
            del(my_dict[fruits[i]])
        i+=1
        
    if len(my_dict)<=2:
        max_count= max(max_count, j-i+1)
    
print(max_count)
    
#This is the optimal sol time comp is O(N).        
    