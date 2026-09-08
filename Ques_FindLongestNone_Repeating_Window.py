#Topic Sliding window and two pointer approch.
#Ques Longast Substring without repeating charaters.

s="CADBZABCD"
i=0

max_count=0
seen= set()

for j in range(len(s)):
    while s[j]  in seen:
        seen.remove(s[i])
        i+=1
    seen.add(s[j])
    
    
    max_count=max(j-i+1, max_count)
  
print(max_count)
#Here time comp is O(N).