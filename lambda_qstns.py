"""Q1 count the odd numbergiven list  using lambda expression
          list1 = [10, 21, 4, 45, 66, 93, 11]"""
list1=[10,21,4,45,66,93,11]
n= len(list(filter(lambda x: x % 2 != 0, list1)))
print(n)


"""Q2 Python program to print odd Numbers in a List using Using List Comprehension 
        list1 = [10, 21, 4, 45, 66, 93, 11]"""
list2=[10,21,4,45,66,93,11]
l_odd=[i for i in list2 if i%2!=0]
print(l_odd)

#Q3 string1 = "Hello World" split this string1 using lambda function
"""string1="Hello World"
n=split(filter(lambda x:'',string1))
print(n)"""


#Q4 my_dict = {'a': 1, 'b': 2, 'c': 3}  add the values of a dictionary using lambda function
my_dict={'a':1,'b':2,'c':3}
from functools import *
add_values=reduce(lambda x, y: x + y, my_dict.values())
print(add_values)

"""Q5 list3 = [1, 2, 3, 4]
       list4 = [5, 6, 7, 8]
      add this two list using lambda function"""
list3=[1,2,3,4]
list4=[5,6,7,8]
add_lists=list(map(lambda x,y:x+y,list3,list4))
print(add_lists)

"""Q6 calculate the total multiplication of all elements in a list use lambda function
      my_list = [1, 2, 3, 4, 5]"""
my_list = [1, 2, 3, 4, 5]
from functools import *
multiply=reduce(lambda x,y:x*y,my_list)
print(multiply)


"""Q7 calculate the total addition of all elements in a list use lambda function
         my_list = [1, 2, 3, 4, 5]"""
my_list1 = [1, 2, 3, 4, 5]
from functools import *
multiply1=reduce(lambda x,y:x+y,my_list1)
print(multiply1)

"""Q8  my_string = "Hello   World" remove space inside a string using a lambda function
 
           o/p== HelloWorld"""
my_string="Hello world"
output=filter(lambda x:" "!=0,my_string)
print(output)

