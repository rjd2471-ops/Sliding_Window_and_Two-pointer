#Ques Find the maximum conscetive one and you can convert k zeros into one.

s=[1,1,1,0,0,0,1,1,1,1,0]
k=2


max_ones=0
for i in range(len(s)):
    zeros=0
    for j in range(i, len(s)):
        if s[j]==0:
            zeros+=1
        
        if zeros>k:
            break
        max_ones= max(max_ones,j-i+1)
            
print(max_ones)
#This is the brute force approch for this is and here time comp is O(N**2) and space comp is O(1).

#Let's try the better sol for this._____________________________________________________________________.


s=[1,1,1,0,0,0,1,1,1,1,0]
k=2
i=0
max_ones=0
zeros=0
for j in range(len(s)):
    
    if s[j]==0:
        zeros+=1
        
    while zeros>k:
        if s[i]==0:
           zeros-=1
        i+=1
    max_ones= max(max_ones,j-i+1)
    
print(max_ones)

#This is the better sol for this and here time comp is O(N) and space comp is O(1).


#Let's try the optimal sol for this._____________________________________________________________________.


s=[1,1,1,0,0,0,1,1,1,1,0]
k=2
i=0
max_ones=0
zeros=0
for j in range(len(s)):
    
    if s[j]==0:
        zeros+=1
        
    if zeros>k:
        if s[i]==0:
           zeros-=1
        i+=1
    if zeros<= k:
       max_ones= max(max_ones,j-i+1)
    
print(max_ones)

#This is the optimal sol for this and here time comp is O(N) and space comp isO(1).