Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d = {'a':1 , 'b': 2}
d
{'a': 1, 'b': 2}
len(d)
2
1 in d
False
'a' in d
True

d2 = {'a':1 , 'b': 2, 'c' : 3}
d2
{'a': 1, 'b': 2, 'c': 3}
d2.keys()
dict_keys(['a', 'b', 'c'])
d2.values()
dict_values([1, 2, 3])
list(d2.keys())
['a', 'b', 'c']
list(d2.values())
[1, 2, 3]
d2.items()
dict_items([('a', 1), ('b', 2), ('c', 3)])
list(d2.items())
[('a', 1), ('b', 2), ('c', 3)]
for x in d.keys():
    print(d[x])

    
1
2
for x in d.keys():
    print(x,d[x])

    
a 1
b 2



for x in d.items():
    print(x)

    
('a', 1)
('b', 2)
for key.values in d.items():
    print(key.values)

    
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    for key.values in d.items():
NameError: name 'key' is not defined
for key.values in d.items():
    print(key,values)

    
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    for key.values in d.items():
NameError: name 'key' is not defined
#like x,y
for key,values in d.items():
    print(key,values)

    
a 1
b 2
d2['a'] = [1,2,3]
d2
{'a': [1, 2, 3], 'b': 2, 'c': 3}
del d['b']
d
{'a': 1}
>>> d2.get('a')
[1, 2, 3]
>>> 
>>> #update
>>> d2
{'a': [1, 2, 3], 'b': 2, 'c': 3}
>>> d3 = {'d': 4 , 'e': 7}
>>> d2.update(d3)
>>> d2
{'a': [1, 2, 3], 'b': 2, 'c': 3, 'd': 4, 'e': 7}
>>> d2.update(e = 200)
>>> d2
{'a': [1, 2, 3], 'b': 2, 'c': 3, 'd': 4, 'e': 200}
>>> #
>>> d2.setdefault('g'100)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> d2
{'a': [1, 2, 3], 'b': 2, 'c': 3, 'd': 4, 'e': 200}
>>> d2.setdefault('g':100)
SyntaxError: invalid syntax
>>> d2.setdefault('g',100)
100
>>> d2
{'a': [1, 2, 3], 'b': 2, 'c': 3, 'd': 4, 'e': 200, 'g': 100}
>>> d2.setdefault('c'300)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> d2.setdefault('c',300)
3
>>> d2
{'a': [1, 2, 3], 'b': 2, 'c': 3, 'd': 4, 'e': 200, 'g': 100}
>>> d2.setdefault('c',3000)
3
>>> d2
{'a': [1, 2, 3], 'b': 2, 'c': 3, 'd': 4, 'e': 200, 'g': 100}
>>> d2.setdefault('b',3000)
2
>>> d2
{'a': [1, 2, 3], 'b': 2, 'c': 3, 'd': 4, 'e': 200, 'g': 100}
