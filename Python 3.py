#!/usr/bin/env python
# coding: utf-8

# <h2> Python with reference to ML and Data Science</h2>

# In[36]:



my_list = [1, 2, 3]

my_list.append(4)                    #appending the list (end)
print("After append : ", my_list)

my_list.extend([5, 6, 7, 8, 2])
print("After extend : ", my_list)  #extending the list

my_list.insert(1, 8)                  #inserting an element in list at particular index
print("After insert : ", my_list)

my_list.remove(2)                    #removing an element from the list
print("After remove : ", my_list)

popped_item = my_list.pop(2)           #popping the item
print("After pop : ", my_list, "Popped Item : ", popped_item)

index = my_list.index(6)
print("List : ", my_list)
print("Index is : ", index)

count = my_list.count(8)
print("Count is :", count )

print("Before sort List : ", my_list)
my_list.sort()
print("After sort List : ", my_list)

my_list.reverse()
print("Reversed List : ", my_list)

my_list.clear()
print("Cleared List : ", my_list)


# <h3> Some other use of built in functions</h3>

# In[19]:


#stripped function
my_string = ("RED WINE tASTEs GOOD WheN&& chilled&*&")

splt = my_string.split()    #split based on character , white space by default, etc
print("After Split : ", splt)

join_str = ' '.join(splt)          #join words / sentences to form a single striung
print("Joined String is : ", join_str)


stripped_string = my_string.strip('&')  #Removes leading and trailing character (space by default)
print("abced", stripped_string)

upper_case = my_string.upper()  #Capitalizing all the words
print("Upper : ", upper_case)

lower_case = my_string.lower() #lower casing all the words
print("Lower : ", lower_case)


# In[ ]:




