#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Fibonacci without using functions :

n = int(input("Enter numbers: "))
a = 0 
b = 1
print("Fibonacci:", a, b, end=" ")

for i in range(n - 2):
    
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    



# In[2]:


#CLASS
#ADVANTAGES of class 
class nav:
    def __init__(self,name,age):     #constructor
       
        self.name = name
        self.age = age
        
    def conf(self):
        print("Details are :", self.name, self.age)
        
 
        
ob1 = nav("Tushar",32)
ob2 = nav("Rahul", 32)


ob1.conf()
ob2.conf()





# In[26]:


class student:                         #class inside class (inner class)
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
        
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
        
    class laptop:
        
            def __init__(self):
                self.brand = "DELL"
                self.ram = 16
                
                
            def show(self):
                print(self.brand, self.ram)
                
ob1 = student("tushar", 2)
ob1.show()





# In[4]:


#SORTING

#BUBBLE SORT  #[1,5,3,2,6]  [1,3,2,5,6]
 
def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
            else :
                pass
    
    
    
nums = [ 10, 5, 8, 6, 2]  #[ 5,10,8,6,2] [ 5 8 10 6 2 ] [ 5 8 6 10 2] [ 5 8 6 2 10 ] [ 2 5 6 8 10]
sort(nums)
print("Sorted List :", nums)


# In[5]:


#selection sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        temp = arr[i]
        arr[i] = arr[min_idx] 
        arr[min_idx] = temp
    return arr


arr = [64, 25, 12, 22, 11] #[11 , 25 , 12 ,22, 64] # [ 11, 12, 25, 22, 64 ] [ 11 12 22 25 64]
print(selection_sort(arr))


# In[6]:


# Quick sort divide and conquer

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [i for i in array if i < pivot]
    middle = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]

    return quicksort(left) + middle + quicksort(right)


array = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(array))


# In[7]:


#Inheritance 

class apex:
    def meth1(self):
        print("I am Initial 1")
        
    def meth2(self):
        print("I am Initial 2")
        
class base(apex):
    def meth3(self):
        print("I am Initial 3")
        
    def meth4(self):
        print("I am Initial 4")
class nex(base):
    pass
        
ob1 = apex()
ob2 = base()
ob3 = nex()

ob1.meth1()
ob2.meth1()
ob3.meth1()


# In[8]:


#constructor and super keyword in inheritance :
class apex:
    
    def __init__(self):
        print("I am self")
    def meth1(self):
        print("I am Initial 1")
        
    def meth2(self):
        print("I am Initial 2")
        
class base(apex):
    def __init__(self):
        super().__init__()
        print("I am Base")
    def meth3(self):
        print("I am Initial 3")
        
    
ob1 = base()

ob1.meth3()
        


# In[30]:


#operator overloading
class stud:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = stud(x,y)
        return z

s1 = stud(2, 3)
s2 = stud(5, 7)
s3 = stud(5, 8)

z = s1 + s2 + s3
print(z.x, z.y) 


# In[10]:


#method overloading
class student:
   
    def __init__(self):
        pass     
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s
    
ob1 = student()

print(ob1.sum(1,21))
    


# In[11]:


#method overriding

class animal:
    def sound(self):
        print("I am sound")

class dog(animal):
    def sound(self):
        print("Bark!")


animal = animal()
animal.sound()  

dog = dog()
dog.sound() 


# In[42]:


#exception handling

a = 10
b = 2
try :
    print("Execution Started")
    print(a/b)
    c = int(input("Enter a number : "))
    
except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Error : Enter a number")
    
except Exception: 
    print("Enter valid data")
    
finally : 
    print("Ended")


# In[33]:


#file handling
#reading a file
file = open('C:/Users/UTU3KOR/Downloads/newt.txt','r')
print(file.read())
print(file.readline())


# In[39]:


#writing in file
f2 = open('C:/Users/UTU3KOR/Downloads/abc','w')
f2.write('laptop')
f2.write('\n New')


# In[41]:


#append in file
#writing in file
f2 = open('C:/Users/UTU3KOR/Downloads/abc','a')

f2.write('\n'+'Hello')

