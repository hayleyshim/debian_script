#!/usr/bin/python3

n = len("Hello World")
print(n)

str1 = 'blue'
str2 = 'blue'
str3 = 'sky'
s = str1 + str2

print(s)

if str1 == str2:
    print("str1 and str2 are same")
if str1 is str2:
    print("str1 and str2 are same")
if str1 != str3:
    print("str1 and str3 are not same")
if str1 is not str3:
    print("str1 and str3 are not same")


str1 = "Blue"
str2 = "BLUE"
str3 = "sky"
if str1.lower() == str2.lower():
    print("str1 and str2 are same")
if str1.lower() != str3.lower():
    print("str1 and str3 are not same")



str = "helloworld"
sub = str[2:5]
c = str.count("l")
print(sub)
print(c)

str = "running"
idx = str.find("nn")
idx = str.rfind("ing")

str = "running"
if str.startswith("run"):
    print("starts with run")
if str.endswith("ing"):
    print("ends with ing")

s = "Hello World"
l = s.lower()
print(l)
l = s.upper()
print(l)

s = "Hello World"
s2 = s.replace("Hello", "New")

s = "a:b:c"
s2 = s.split(":")
print(s2)

s = " vim "
s2 = s.strip()
print(s2)

s = "text"
if s.isalnum():
    print("Contatins only alphanumeric characters")
if s.isalpha():
    print("Contains only alphabetic characters")
if s.isdigit():
    print("Contains only digits")
if s.isspace():
    print("Contains only whitespace characters")
if s.isupper():
    print("Contains only uppercase characters")
if s.islower():
    print("Contains only lowercase characters")

"""
s = str(268)
print(type(s))
s = str(22.7)
print(type(s))
s = str([1,2,3])
print(type(s))
s = str({'a': 1, 'b':2})
print(type(s))
"""
x = 10
y = eval("x * 2")
print(y)
n = eval("min([4,3,4])")

exec("for i in range(5):\n print(i)\n")

#print("Ordinal value of 'a' is " + str(ord("a")))
print("Character with value 65 is " + chr(65))

l = [ord(i) for i in "Hello"]
s = ''.join(chr(i) for i in l)
print(s)
print(l)


