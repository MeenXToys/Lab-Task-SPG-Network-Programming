import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
z = re.findall('[^0-9]+', x)
a = re.findall('[AEIOU]+', x)
print(y)
print(z)
print(a)

x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print (y)

c = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
c = re.findall('^From (\S+@\S+)', x)
print(c)
