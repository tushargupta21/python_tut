#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#IF ELIF ELSE
a = int(input("Enter the age"))
if 60 > a >= 18 :
    print("Adult :", a)
elif 0 < a < 18:
    print("Kid : ", a)
elif 60 <= a :
    print("Old", a)
else:
    print("Please Enter Valid Age", a)


# In[2]:


#FOR_LOOP

for i in range(10):
    
    print(i * ' *')
    


# In[2]:


#WHILE LOOP
i = 1
n = 10
while i<n:
    print(i * " *")
    i = i  + 1


# In[ ]:


#SWAP 2 numbers

a = input("Enter a number : ")
b = input('Enter number :')

temp = a #temp =4
a = b     #a =5
b = temp   #b =4
print (a, b)

# a = a + b  a =9
# b = a - b  b = 4
# a = a - b a = 5


# In[ ]:


#BREAK 

lot = 10

x = int(input("Enter book requested : "))
i = 1
while i<= x:
    
    if i > lot:
        print("Books quantity ended")
        break
    i += 1
    
    print ("Book")


# In[7]:


#continue 

for i in range(1,50):

    if i%3 == 0 or i%5 == 0:
        continue
    
    print(i)
    

 


# In[ ]:


#pass 
for i in range(10):
    if i % 2 == 0:
        pass 
    else:
        print(i)


# In[ ]:


#FUNCTION def fun_name(parameters):
c = 10                             #global
def add_sub(a,b):
    global c 
    c = a + b
    d = a - b
    return c, d
   
result1, result2 = add_sub(4,5)
print(c)
print(result1, result2)


# In[ ]:


a = 0 
b = 1


# In[8]:


#FIBBONNACI SERIES


def fibonacci(n):
    fb_lst = [0, 1] # {0,1,1, 2, 3}
    while len(fb_lst) < n:
        fb_lst.append(fb_lst[-1] + fb_lst[-2])
    return fb_lst

n = 10
result = fibonacci(n)
print(result)


# In[9]:


#FACTORIAL

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)  #5 * 4! #4*3! 5 *4 *3 *2 *1


result = factorial(5)
print("The factorial of 5 is:", result)


# In[15]:


#CLASS AND OBJECT
class computer:
    def det(self):
        print('DELL')
        
ob1 = computer()    #object

ob1.det()     #calling method
        
        


# In[ ]:


#SORTING

#BUBBLE SORT  #[1,5,3,2,6] [1,3,2,5,6]
 
def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    
    
    
nums = [ 10, 5, 8, 6, 2]
sort(nums)
print("Sorted List :", nums)


# In[ ]:


#SORTING

#BUBBLE SORT  #[1,5,3,2,6] [1,3,2,5,6]
 
def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    
    
    
nums = [ 10, 5, 8, 6, 2]
sort(nums)
print("Sorted List :", nums)


# In[ ]:




