#!/usr/bin/env python
# coding: utf-8

# In[12]:


file_path = open('/Users/mac/Downloads/python.txt', 'r')
print(file_path.read())


# In[18]:


with open('/Users/mac/Downloads/python.txt', 'r') as file:
    read_lines = file.readline()
    print(read_lines)


# In[ ]:




