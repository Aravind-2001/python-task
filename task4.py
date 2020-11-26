Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[]
>>> print("blank list:")
blank list:
>>> list=[10,30,60,40,20,50,70,100,90]
>>> print(list)
[10, 30, 60, 40, 20, 50, 70, 100, 90]
>>> list.insert(4,80)
>>> print(list)
[10, 30, 60, 40, 80, 20, 50, 70, 100, 90]
>>> list=[10, 30, 60, 40, 80, 20, 50, 70, 100, 90]
>>> list.remove(40)
>>> print(list)
[10, 30, 60, 80, 20, 50, 70, 100, 90]
>>> list=[10, 30, 60, 80, 20, 50, 70, 100, 90]
>>> print("the list is:",max(list))
the list is: 100
>>> print("the list is:",min(list))
the list is: 10
>>> 