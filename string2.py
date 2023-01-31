Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> w="aaa,bbb,ccc"
>>> w
'aaa,bbb,ccc'
>>> w.split(',')
['aaa', 'bbb', 'ccc']
>>> w.split('spam')
['aaa,bbb,ccc']
>>> w.split()
['aaa,bbb,ccc']
>>> w="aaa,bbb,,,ccc"
>>> w.split(' ,')
['aaa,bbb,,,ccc']
>>> w="asfghjkspamkloiujhg"
>>> w.split(',')
['asfghjkspamkloiujhg']
>>> w.split('spam')
['asfghjk', 'kloiujhg']
>>> w="asfghjkspamklospamiujhg"
>>> w.split('spam')
['asfghjk', 'klo', 'iujhg']
>>> w.rsplit('spam',1)
['asfghjkspamklo', 'iujhg']
>>> x
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x="Hello"
>>> x
'Hello'
>>> x.lower()
'hello'
>>> x.upper()
'HELLO'
>>> x.capitalize()
'Hello'
