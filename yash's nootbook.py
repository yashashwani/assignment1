


#assigning elements to different lists
names = ['yash','jhon','steve','alex']
print(names)



names = ['yash','jhon','steve','alex']
print(names)
name1 = names.copy()
name1.append('rock')
print(name1)


# In[10]:


numbers = ['1','4','7']
print(numbers)


# In[13]:


numbers = ['1','4','7']
numbers[2]='9'
print(numbers)
numbers.insert(1,20)
print(numbers)


# In[17]:


#accessing elements from a tuple.
numbers = (1,4,8,9)
print(numbers[2])


# In[18]:


coordinates = (1,4,8)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x,z)


# In[22]:


#deleting different dictionary elements.
customer = {
    "name":"yash ashwani",
    "age":"19  ",
    "is_certified":True
}
print(customer["name"])


# In[23]:


customer = {
    "name":"yash ashwani",
    "age":"19  ",
    "is_certified":True
}
print(customer["name"])
del customer["is_certified"]
print(customer)


# In[ ]:




