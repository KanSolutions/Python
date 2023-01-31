Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x='hello'
x
'hello'
x.find('o')
4
x.index('h')
0
#strip
#to remove spaces
y = " abc bcd cde "
y.strip()
'abc bcd cde'
y.strip(" ")
'abc bcd cde'
y.strip("abc")
' abc bcd cde '
y.strip("abc.")
' abc bcd cde '
y.strip('abc.')
' abc bcd cde '
y.rstrip('abc.')
' abc bcd cde '
a =  "www.example.com"
a.strip('w.')
'example.com'
y.rstrip('a.')
' abc bcd cde '
y.strip('a.')
' abc bcd cde '
x
'hello'
x.center(10)
'  hello   '
x.center(10, '_')
'__hello___'
x.ljust(10,'_')
'hello_____'
x.rjust(10,'_')
'_____hello'
x.zfill('a')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x.zfill('a')
TypeError: 'str' object cannot be interpreted as an integer
x.zfill(10)
'00000hello'
a
'www.example.com'
a.partition('.')
('www', '.', 'example.com')
a.split('.')
['www', 'example', 'com']
a.split('.', 1)
['www', 'example.com']
e = 'first line \n second line \n'
e
'first line \n second line \n'
e.splitlines()
['first line ', ' second line ']
e.splitlines(True)
['first line \n', ' second line \n']
#dictionary

m = {'var' : 'Hello'}
m['var']
'Hello'
'value of var is %(var)'%(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    'value of var is %(var)'%(a)
TypeError: format requires a mapping
'value of var is %(var)'%(m)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    'value of var is %(var)'%(m)
ValueError: incomplete format
'value of var is %(var)s'%(a)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    'value of var is %(var)s'%(a)
TypeError: format requires a mapping
'value of var is %(var)s'%(m)
'value of var is Hello'
vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 'hello', 'y': ' abc bcd cde ', 'a': 'www.example.com', 'e': 'first line \n second line \n', 'm': {'var': 'Hello'}}
####strinf4
###################3
L  = [1,2,3]
"List daa = {}".format(L)
'List daa = [1, 2, 3]'
str1 = "List daa = {}".format(L)
str1
'List daa = [1, 2, 3]'
str1.replace('1','19')
'List daa = [19, 2, 3]'
d=100
hex(d),oct(d),bin(d)
('0x64', '0o144', '0b1100100')
'{0},{0},{0}'.format(d)
'100,100,100'
'{0:x},{0:o},{0:b}'.format(d)
'64,144,1100100'
ompl = 3+7j
"".format(ompl)
''
comp = 3+7j
"{}".format(c)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    "{}".format(c)
NameError: name 'c' is not defined
comp = 3+7j
'{}'.format(comp)
'(3+7j)'
D = 100
D
100
D = {"variable" : 100}
"{d[variable]}",format(d=D)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    "{d[variable]}",format(d=D)
TypeError: format() takes no keyword arguments
'{d[variable]}'.format(d=D)
'100'
'{d[variable]}'.format(d={"variable" : 100})
'100'
import sys
sys.platform
'win32'
'{[variable]} {sys.platform}'.format({"variable" : 100}, sys=sys)
'100 win32'
D = {"variable" : 100, 'name': 'vk'}
D
{'variable': 100, 'name': 'vk'}
'{variable}{name}'.format(D)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    '{variable}{name}'.format(D)
KeyError: 'variable'
'{variable}{name}'.format(D)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    '{variable}{name}'.format(D)
KeyError: 'variable'
'{variable}{name}'.format(**D)
'100vk'
'%r'%('spam')
"'spam'"
'%s'%('spam')
'spam'
'{0!r}{0!s}'.format('spam')
"'spam'spam"
import datetime
x.datetime.now()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    x.datetime.now()
AttributeError: 'str' object has no attribute 'datetime'

datetime.datetime.now()
datetime.datetime(2023, 1, 28, 9, 14, 26, 484444)
dt = datetime.datetime.now()
dt
datetime.datetime(2023, 1, 28, 9, 15, 3, 334523)
'{}'.format(dt)
'2023-01-28 09:15:03.334523'
'{:y}'.format(dt)
'y'
'{%y}'.format(dt)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    '{%y}'.format(dt)
KeyError: '%y'
'{:%y}'.format(dt)
'23'
'{:%Y %m %d}'.format(dt)
'2023 01 28'
'{%y %m %d %H %m %S}'.format(dt)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    '{%y %m %d %H %m %S}'.format(dt)
KeyError: '%y %m %d %H %m %S'
'{%y %m %d %H %M %S}'.format(dt)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    '{%y %m %d %H %M %S}'.format(dt)
KeyError: '%y %m %d %H %M %S'
'{:%y :%m :%d :%H :%m :%S}'.format(dt)
'23 :01 :28 :09 :01 :03'
'{:%y :%m :%d :%H :%m :%S :%a
}'.format(dt)
SyntaxError: unterminated string literal (detected at line 1)
'{:%y :%m :%d :%H :%m :%S :%a}'.format(dt)
'23 :01 :28 :09 :01 :03 :Sat'
'{:%y :%m :%d :%H :%m :%S :%a %b}'.format(dt)
'23 :01 :28 :09 :01 :03 :Sat Jan'
#string5
f'name : {name] Age {age} Salary: {salary}'
SyntaxError: f-string: unmatched ']'
f'name : {name] age {age} salary: {salary}'
SyntaxError: f-string: unmatched ']'
f'Name : {Name] Age {Age} Salary: {Salary}'
SyntaxError: f-string: unmatched ']'
Name= 'champa'
Age=25
Salary= 100.00
f'Name : {Name] Age {Age} Salary: {Salary}'
SyntaxError: f-string: unmatched ']'
f"Name : {Name] Age {Age} Salary: {Salary}"
SyntaxError: f-string: unmatched ']'


apples=10
cost=20
f"total cost of {apples} apples @ {cost} is {apples*cost}"
'total cost of 10 apples @ 20 is 200'
def cost(apples,cost):
    return apples*cost
f"total cost of {apples} apples @ {cost} is {cost()}"
SyntaxError: invalid syntax
f"total cost of {apples} apples @ {cost} is {cost(apples,cost)}"
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    f"total cost of {apples} apples @ {cost} is {cost(apples,cost)}"
TypeError: 'int' object is not callable
f"total cost of {apples} apples @ {cost} is {cost(apples},{cost})}"
SyntaxError: f-string: closing parenthesis '}' does not match opening parenthesis '('
>>> f"total cost of {apples} apples @ {20} is {cost(apples,20)}"
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    f"total cost of {apples} apples @ {20} is {cost(apples,20)}"
TypeError: 'int' object is not callable
>>> f"name in upper is{name.upper()}"
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    f"name in upper is{name.upper()}"
NameError: name 'name' is not defined. Did you mean: 'Name'?
>>> f"name in upper is{Name.upper()}"
'name in upper isCHAMPA'
>>> f"name in upper is {name.upper()}"
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    f"name in upper is {name.upper()}"
NameError: name 'name' is not defined. Did you mean: 'Name'?
>>> f"name in upper is {Name.upper()}"
'name in upper is CHAMPA'
>>> from string import Template
>>> t =  Template('my name is $Name)
...               
SyntaxError: unterminated string literal (detected at line 1)
>>> t =  Template('my name is $Name')
...               
>>> t
...               
<string.Template object at 0x000001517B0C40D0>
>>> t.substitute(Name = 'vrushi')
...               
'my name is vrushi'
>>> t=Template('Name is ${Name}shi')
...               
>>> t
...               
<string.Template object at 0x000001517B69CA90>
>>> t.substitute(Name = 'V')
...               
'Name is Vshi'
