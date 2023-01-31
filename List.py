Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l = list()
l
[]
l1= [3 ,6, 9]
l1
[3, 6, 9]
l2= ['a','b','c']
l2
['a', 'b', 'c']
l2 = l1
l2
[3, 6, 9]
l2 = ['a', 'b', 'c'l1]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l2 = ['a', 'b', 'c',l1]
l2
['a', 'b', 'c', [3, 6, 9]]
s = 'spam'
[x*4 for x in s]
['ssss', 'pppp', 'aaaa', 'mmmm']
for x in s:
    x

    
's'
'p'
'a'
'm'
l = []
for x  in s:
    l.append(x*4)

    
l
['ssss', 'pppp', 'aaaa', 'mmmm']
[x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
len(l)
4
min(l1)
3
max(l1)
9
sum(l1)
18
for x in l
SyntaxError: expected ':'
for x in l:
    x

    
'ssss'
'pppp'
'aaaa'
'mmmm'
3 in l1
True
 'ssss' in l
 
SyntaxError: unexpected indent
'ssss' in l[]
SyntaxError: invalid syntax
'a' in l2
True
l+ list("cccc")
['ssss', 'pppp', 'aaaa', 'mmmm', 'c', 'c', 'c', 'c']
l+'c'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    l+'c'
TypeError: can only concatenate list (not "str") to list
l+list('b')
['ssss', 'pppp', 'aaaa', 'mmmm', 'b']
l
['ssss', 'pppp', 'aaaa', 'mmmm']
len(l)
4
l1
[3, 6, 9]
l[0] = 10
l1[0] = 1
l1[0] = 10
l1
[10, 6, 9]
l1[0:2]
[10, 6]
l1[0:2] = [20,30,40,50]
l1
[20, 30, 40, 50, 9]
len(l1)
5
l[len(l1): len(l1)] = [100,100]
l1[len(l1): len(l1)] = [100,100]
l1
[20, 30, 40, 50, 9, 100, 100]
l1.append(9)
l1
[20, 30, 40, 50, 9, 100, 100, 9]
l1.extend('spam')
l1
[20, 30, 40, 50, 9, 100, 100, 9, 's', 'p', 'a', 'm']
l1.insert(4,60)
l1
[20, 30, 40, 50, 60, 9, 100, 100, 9, 's', 'p', 'a', 'm']
>>> l1.pop()
'm'
>>> l1
[20, 30, 40, 50, 60, 9, 100, 100, 9, 's', 'p', 'a']
>>> l1.pop(5)
9
>>> l1
[20, 30, 40, 50, 60, 100, 100, 9, 's', 'p', 'a']
>>> l1.remove('a')
>>> l1
[20, 30, 40, 50, 60, 100, 100, 9, 's', 'p']
>>> del l1[5:7]
>>> l1
[20, 30, 40, 50, 60, 9, 's', 'p']
>>> l1.clear()
>>> l1
[]
>>> t = (1,2,3,4,5,6)
>>> list(t)
[1, 2, 3, 4, 5, 6]
>>> for x in t:
...     l1.append(x)
... 
...     
>>> l1
[1, 2, 3, 4, 5, 6]
>>> l2 = l1.sort()
>>> l2
>>> 
>>> l1 = [3,6,8,1,2,5]
>>> l2 = l1.sort()
>>> l2
>>> l2 = ['b','t','a']
>>> l2.sort()
>>> l2
['a', 'b', 't']
>>> l2.sort(reverse= True)
>>> l2
['t', 'b', 'a']
