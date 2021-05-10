#!/usr/bin/env python
# coding: utf-8

# In[2]:


def minFlips(target):
    curr='1'
    count=0
    
    for i in range(len(target)):
        
        if target[i]==curr:
            count+=1
            
            curr=chr(48+(ord(curr)+1)%2)
        
    return(count)

S="011000"
print(minFlips(S))


# In[5]:


def minFlips(target):
    curr='1'
    count=0
    
    for i in range(len(target)):
        
        if target[i]==curr:
            count+=1
            continue
        
    return(count)

S="011000"
print(minFlips(S))


# In[7]:


def sumofminabdiff(arr,n):
    arr.sort()
    sum=0
    sum+=abs(arr[0]-arr[1])
    sum+=abs(arr[n-1]-arr[n-2])
    
    for i in range(1,n-1):
        sum+=min(abs(arr[i]-arr[i-1]),abs(arr[i]-arr[i+1]))
        
    return(sum)

arr=[5,10,1,4,8,7]
n=len(arr)
print("Sum is: ",sumofminabdiff(arr,n))


# In[ ]:




