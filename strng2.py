Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#find and index
x="hello world'
SyntaxError: unterminated string literal (detected at line 1)
x='hello world'
x.find('0')
-1
x.find('o')
4
x.find('o',5)
7
x.find('l',3,10)
3
x.find('l',4,10)
9
#If the value is not found, the find() method returns -1, but the index() method will raise an exception:
x.index('w')
6
l = list(x)
l
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
",".join(1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ",".join(1)
TypeError: can only join an iterable
','.join(l)
'h,e,l,l,o, ,w,o,r,l,d'
"champa".join(l)
'hchampaechampalchampalchampaochampa champawchampaochamparchampalchampad'
l[0:3]
['h', 'e', 'l']
y="champa".join(l)
y
'hchampaechampalchampalchampaochampa champawchampaochamparchampalchampad'
y.split()
['hchampaechampalchampalchampaochampa', 'champawchampaochamparchampalchampad']
y.split(',')
['hchampaechampalchampalchampaochampa champawchampaochamparchampalchampad']
x
'hello world'
x.upper()
'HELLO WORLD'
x.lower()
'hello world'

x.capitalize()
'Hello world'
x.swapcase()
'HELLO WORLD'
>>> x.title()
'Hello World'
>>> x=''hello
SyntaxError: invalid syntax
>>> x='hello'
>>> x.title()
'Hello'
>>> x.startswith("h")
True
>>> x.startswith('l',2)
True
>>> x.startswith('l',1)
False
>>> x.startswith('l'4)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> x.startswith('l',4)
False
>>> x.endswith("o")
True
>>> x.count('l')
2
>>> x.encode('utf-8')
b'hello'
>>> x.decode()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> y=x.encode('utf-8')
>>> y
b'hello'
>>> 
>>> y=x.decode()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    y=x.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> y.decode()
'hello'
>>> #string3
