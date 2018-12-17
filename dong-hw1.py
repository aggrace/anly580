
# coding: utf-8

# In[1]:

from nltk.book import *


# In[7]:

text2


# In[15]:

#Question 2
len(text2)


# In[18]:

len(set(text2))
#141576 words in total, number of distinct words is 6833


# In[16]:

##Question 4

text2.dispersion_plot(["Elinor","Marianne","Edward","Willoughby"])
##From the plot we can see that the story is about Elinor and Marianne. However the Edward and Will are not as much 
#mentioned as two female, Elinor and Edward may be a couple, and another couple may be Marianne and Willoughby


# In[31]:

#Question 22
fourwords=[w for w in set(text5) if len(w)==4]
sorted(fourwords)
fdist1=FreqDist(fourwords)
fdist1.most_common()


# In[64]:

#23
#sorted(w for w in set(text6) if w.isupper())
for w in set(text6):
    if w.isupper():
        print(w)


# In[62]:

#24
sorted(a for a in set(text6) 
       if a.istitle()       
      and  a.endswith('i') or a.endswith('z') or a.endswith('e')
      and 'z' in a
      and 'ze' in a
      )


# In[88]:

#28 
#from __future__ import print_function
def percent(word,text):
    occurance=text.count(word)
    total=len(text)
    return str(100 * occurance/total) + '%'


# In[90]:

##Example
print(percent("love", text2))


# In[ ]:




# In[ ]:



