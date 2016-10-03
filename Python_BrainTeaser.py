
# coding: utf-8

# In[22]:

def letter_count(st):
    d = {"Upper":0,"Lower":0}
    for c in st:
        if c.isupper():
            d['Upper']+=1
        elif c.islower():
            d['Lower']+=1
        else:
            pass
    print d["Upper"]
    print d["Lower"]
    
           


# In[23]:

st = "Find Upper and lower case letters in the Given String"
letter_count(st)


# Q.  Find Unique Number in the given list

# In[24]:

def uniqueList(l):
    x = []
    for c in l:
        if c not in x:
            x.append(c)
    return x


# In[25]:

l = [1,1,1,1,1,1,2,2,2,3,3,3,5,5,6,6,6,3,8,9,9,9,10]
uniqueList(l)


# Q. Check if the number is palindrome

# In[26]:

def palindrome(s):
    return s == s[::-1]


# In[30]:

palindrome('MiM')


# In[ ]:



