Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 3
>>> print ("x")
x
>>> x=3
>>> print ("x")
SyntaxError: multiple statements found while compiling a single statement
>>> numero = 3
>>> print (numero)
3
>>> name = input(" enter your name: ")
 enter your name: ana
>>> name
'ana'
>>> a = 3
>>> b = 5
>>> print (a*b)
15
>>> c = input (" give a value: ")
 give a value: 5
>>> a == c
False
>>> b == c
False
>>> b
5
>>> c
'5'
>>> d = input ( )
5
>>> d ==b
False
>>> d
'5'
>>> b = '5'
>>> b
'5'
>>> b == d
True
>>> a <= d
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a <= d
TypeError: unorderable types: int() <= str()
>>> a << b
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a << b
TypeError: unsupported operand type(s) for <<: 'int' and 'str'
>>> a
3
>>> b
'5'
>>> a = '3'
>>> a
'3'
>>> a <= b
True
>>> 
