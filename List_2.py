Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c = [3,6,9,12,15,18,21]
c.count()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    c.count()
TypeError: list.count() takes exactly one argument (0 given)
c.count(2)
0
c.count(1)
0
c.index(2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c.index(2)
ValueError: 2 is not in list
c.count(6)
1
c.index(18)
5
c.index(9,21)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    c.index(9,21)
ValueError: 9 is not in list
c.index(9)
2
c.index(9,15)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c.index(9,15)
ValueError: 9 is not in list
c
[3, 6, 9, 12, 15, 18, 21]
c1 = [2,4,8,[1,3,5]]
c2= c.copy()
c3 = c
>>> c2 is c
False
>>> c2
[3, 6, 9, 12, 15, 18, 21]
>>> c
[3, 6, 9, 12, 15, 18, 21]
>>> c3 is c
True
>>> import copy
>>> c4 = copy.copy(c)
>>> c4
[3, 6, 9, 12, 15, 18, 21]
>>> c4 is c
False
>>> c[-1]
21
>>> ######
>>> #####
>>> #######
>>> 
>>> 
>>> 
>>> c = [1,[]]
>>> c[1].append(1)
>>> c
[1, [1]]
>>> c[0:0]
[]
>>> c
[1, [1]]
>>> c[0:0] = []
>>> c
[1, [1]]
>>> c[0:0] = []
>>> c
[1, [1]]
>>> c[0] = []
>>> c
[[], [1]]
