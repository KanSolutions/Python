Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> D = {}
>>> D
{}
>>> D = dict()
>>> D
{}
>>> D = {'a': 1 , 'b': 2}
>>> D
{'a': 1, 'b': 2}
>>> D.['a']
SyntaxError: invalid syntax
>>> d1 = D['a']
>>> d1
1
>>> D['a']
1
>>> D['b']
2
>>> D['a'] = 3
>>> D
{'a': 3, 'b': 2}
>>> D['b'] = 4
>>> D
{'a': 3, 'b': 4}
