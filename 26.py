Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string2
#Python slice() Function
#A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end
a= "world"
a[0:3]
'wor'
a[:3]
'wor'
a[:]
'world'
a[::-1]
'dlrow'
a[slice(None,None,None)]
'world'
a[slice(0,3,3)]
'w'
a[slice(0,3,2)]
'wr'
#conversions
#string Methods
x='Hello'
x[2] = 'L'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x[2] = 'L'
TypeError: 'str' object does not support item assignment
x[:2]
'He'
y = x[:2] + 'L' +[3:]
SyntaxError: invalid syntax
y = x[:2] + 'L' +x[3:]
y
'HeLlo'
y.replace('l',"L")
'HeLLo'
z="spanhellospanhi"
y= z.replace('spam','hi')
y
'spanhellospanhi'
y= z.replace('span','hi')
y
'hihellohihi'
y= z.replace('span','hi',1)
y
'hihellospanhi'
# 1 is count
#y.find #find for string
x
'Hello'
'Hello'
'Hello'
l= list(x)

l= list(x)

x
'Hello'
l = list(x)
l
['H', 'e', 'l', 'l', 'o']
['H', 'e', 'l', 'l', 'o']
['H', 'e', 'l', 'l', 'o']
l[0] = "h"
l
['h', 'e', 'l', 'l', 'o']
y= str(l)
y
"['h', 'e', 'l', 'l', 'o']"
#join
"".join(l)
'hello'
",".join(l)
'h,e,l,l,o'
y
"['h', 'e', 'l', 'l', 'o']"
y.split()
["['h',", "'e',", "'l',", "'l',", "'o']"]
x
'Hello'
x.split()
['Hello']
a='abc,def'
a
'abc,def'
a.split()
['abc,def']
a.split('')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.split('')
ValueError: empty separator















































































>>> 

... 
>>> 

>>> 

... 
>>> 

>>> 

... 
... 
>>> 

>>> 

... 
>>> 

>>> 

... 
>>> 

>>> 

... 
>>> 

>>> 

... 
>>> 

>>> 

... 





















































































































































































































































































































































































































































































































































































































































