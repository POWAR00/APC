<<<<<<< HEAD
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="Hello"
a
'Hello'
b=100
b
100
type(b)
<class 'int'>
c=3.14
type(c)
<class 'float'>
x=["apple","cherry","Banana"]
type(x)
<class 'list'>
x=("apple","banana")
type(x)
<class 'tuple'>
x=range(9)
type(x)
<class 'range'>
x={"name":"Bhakti","Age":19}
type(x)
<class 'dict'>
x={"apple","banana"}
type(x)
<class 'set'>
x=fronzenset({"apple","banana"})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x=fronzenset({"apple","banana"})
NameError: name 'fronzenset' is not defined. Did you mean: 'frozenset'?
x=frozenset({"apple","banana"})
type(x)
<class 'frozenset'>
x=b"hello
SyntaxError: unterminated string literal (detected at line 1)
x=b"hello"
type(x)
<class 'bytes'>
x=True
type(x)
<class 'bool'>
x=memoryview(bytes(5))
type(x)
<class 'memoryview'>
x=bytearray(5)
type(x)
<class 'bytearray'>
x=None
type(x)
<class 'NoneType'>
x=[10,20,30,40]
type(x)
<class 'list'>
x.append(50)
x
[10, 20, 30, 40, 50]
print(x))
SyntaxError: unmatched ')'
print(x)
[10, 20, 30, 40, 50]
y=(10,20,30)
type(y)
<class 'tuple'>
y.append(40)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    y.append(40)
AttributeError: 'tuple' object has no attribute 'append'
z={"name":"Bhakti","age":34}
z
{'name': 'Bhakti', 'age': 34}
x[2]
30
y[1]
20
z=["name"].append("abc")
z
print(z)
None
x=1j
type(x)
<class 'complex'>
z[1]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    z[1]
TypeError: 'NoneType' object is not subscriptable
z={"name":"bhakti","age":23,"subject":"math"}
type(z)
<class 'dict'>
key[1]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    key[1]
NameError: name 'key' is not defined
z["subject"].append("abc")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    z["subject"].append("abc")
AttributeError: 'str' object has no attribute 'append'
z
{'name': 'bhakti', 'age': 23, 'subject': 'math'}
print(z)
{'name': 'bhakti', 'age': 23, 'subject': 'math'}
x=10,y=20
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
x=10
y=20
x+y
30
x-y
-10
x*y
200
x/y
0.5
x%y
10
x//y
0
x**y
100000000000000000000
x=2
y=4
x+y
6
x-y
-2
x*y
8
x/y
0.5
>>> x//y
0
>>> x%y
2
>>> x**y
16
>>> x=5
>>> x+=3
>>> x
8
>>> x-=3
>>> x
5
>>> x*=3
>>> x
15
>>> x/=3
>>> x
5.0
>>> x%=3
>>> x
2.0
>>> x//=3
>>> x
0.0
>>> x**=3
>>> x
0.0
>>> x=5
>>> x**=3
>>> x
125
>>> x==y
False
>>> x=1
>>> y=1
>>> x==y
True
>>> x!=y
False
>>> x=5
>>> y=8
>>> x>y
False
>>> x<y
True
>>> x>=y
False
x<=y
True
x<5&x<10
False
x<4|x<10
False
x>5|x<10
False
x
5
`
x=10
x<20|x<10
False
y<10|y<5
False
x=3
y=5
x<5|x<10
True
y<10|y>2
True
y<10|y>9
True
x!=6
True
x is y
False
x=10
y=10
x is y
True
x is not y
False
x in y
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    x in y
TypeError: argument of type 'int' is not iterable
x not in y
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    x not in y
TypeError: argument of type 'int' is not iterable
x=["apple","banana","cherry"]
apple in x
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    apple in x
NameError: name 'apple' is not defined. Did you mean: 'tuple'?
print("apple" in x)
True
"abc" in not x
SyntaxError: invalid syntax
"abc" not in x
True
x&y
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x&y
TypeError: unsupported operand type(s) for &: 'list' and 'int'
x=10
y=20
x&y
0
x=0
y=1
x&y
0
x|y
1
x^y
1
x~y
SyntaxError: invalid syntax
x!y
SyntaxError: invalid syntax
x not y
SyntaxError: invalid syntax
~x
-1
~y
-2
x<<y
0
x<<2
0
x=10
x=1
y=0
x<<2
4
y<<2
0
x>>2
0
y>>2
0
x=2
y=1
x<<2
8
y<<2
4
y>>2
0
x>>2
0
=======
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="Hello"
a
'Hello'
b=100
b
100
type(b)
<class 'int'>
c=3.14
type(c)
<class 'float'>
x=["apple","cherry","Banana"]
type(x)
<class 'list'>
x=("apple","banana")
type(x)
<class 'tuple'>
x=range(9)
type(x)
<class 'range'>
x={"name":"Bhakti","Age":19}
type(x)
<class 'dict'>
x={"apple","banana"}
type(x)
<class 'set'>
x=fronzenset({"apple","banana"})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x=fronzenset({"apple","banana"})
NameError: name 'fronzenset' is not defined. Did you mean: 'frozenset'?
x=frozenset({"apple","banana"})
type(x)
<class 'frozenset'>
x=b"hello
SyntaxError: unterminated string literal (detected at line 1)
x=b"hello"
type(x)
<class 'bytes'>
x=True
type(x)
<class 'bool'>
x=memoryview(bytes(5))
type(x)
<class 'memoryview'>
x=bytearray(5)
type(x)
<class 'bytearray'>
x=None
type(x)
<class 'NoneType'>
x=[10,20,30,40]
type(x)
<class 'list'>
x.append(50)
x
[10, 20, 30, 40, 50]
print(x))
SyntaxError: unmatched ')'
print(x)
[10, 20, 30, 40, 50]
y=(10,20,30)
type(y)
<class 'tuple'>
y.append(40)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    y.append(40)
AttributeError: 'tuple' object has no attribute 'append'
z={"name":"Bhakti","age":34}
z
{'name': 'Bhakti', 'age': 34}
x[2]
30
y[1]
20
z=["name"].append("abc")
z
print(z)
None
x=1j
type(x)
<class 'complex'>
z[1]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    z[1]
TypeError: 'NoneType' object is not subscriptable
z={"name":"bhakti","age":23,"subject":"math"}
type(z)
<class 'dict'>
key[1]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    key[1]
NameError: name 'key' is not defined
z["subject"].append("abc")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    z["subject"].append("abc")
AttributeError: 'str' object has no attribute 'append'
z
{'name': 'bhakti', 'age': 23, 'subject': 'math'}
print(z)
{'name': 'bhakti', 'age': 23, 'subject': 'math'}
x=10,y=20
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
x=10
y=20
x+y
30
x-y
-10
x*y
200
x/y
0.5
x%y
10
x//y
0
x**y
100000000000000000000
x=2
y=4
x+y
6
x-y
-2
x*y
8
x/y
0.5
>>> x//y
0
>>> x%y
2
>>> x**y
16
>>> x=5
>>> x+=3
>>> x
8
>>> x-=3
>>> x
5
>>> x*=3
>>> x
15
>>> x/=3
>>> x
5.0
>>> x%=3
>>> x
2.0
>>> x//=3
>>> x
0.0
>>> x**=3
>>> x
0.0
>>> x=5
>>> x**=3
>>> x
125
>>> x==y
False
>>> x=1
>>> y=1
>>> x==y
True
>>> x!=y
False
>>> x=5
>>> y=8
>>> x>y
False
>>> x<y
True
>>> x>=y
False
x<=y
True
x<5&x<10
False
x<4|x<10
False
x>5|x<10
False
x
5
`
x=10
x<20|x<10
False
y<10|y<5
False
x=3
y=5
x<5|x<10
True
y<10|y>2
True
y<10|y>9
True
x!=6
True
x is y
False
x=10
y=10
x is y
True
x is not y
False
x in y
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    x in y
TypeError: argument of type 'int' is not iterable
x not in y
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    x not in y
TypeError: argument of type 'int' is not iterable
x=["apple","banana","cherry"]
apple in x
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    apple in x
NameError: name 'apple' is not defined. Did you mean: 'tuple'?
print("apple" in x)
True
"abc" in not x
SyntaxError: invalid syntax
"abc" not in x
True
x&y
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x&y
TypeError: unsupported operand type(s) for &: 'list' and 'int'
x=10
y=20
x&y
0
x=0
y=1
x&y
0
x|y
1
x^y
1
x~y
SyntaxError: invalid syntax
x!y
SyntaxError: invalid syntax
x not y
SyntaxError: invalid syntax
~x
-1
~y
-2
x<<y
0
x<<2
0
x=10
x=1
y=0
x<<2
4
y<<2
0
x>>2
0
y>>2
0
x=2
y=1
x<<2
8
y<<2
4
y>>2
0
x>>2
0
>>>>>>> 87c005bd6f0afac668a0a3d49f27e47d51161b67
