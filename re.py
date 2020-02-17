import re

#find non space

print(re.findall(r'\S' ,'fycs sycs tycs 123456'))
#find all digits

print(re.findall(r'\d','fycs sycs tycs 123456'))
#find the non digits

print(re.findall(r'\D','fycs sycs tycs 123456'))
#splits

print(re.split(r'\s','fycs fycs tycs 123456'))
#finding whitespaces

print(re.findall(r'\s','fycs fycs tycs 123456'))
#finding start of string

print(re.findall(r'\A','fycs fycs tycs 123456'))
#matching end of strings

print(re.findall(r'\z','fycs fycs tycs 123456'))
#matches a or b

print(re.findall(r'\c|c','fycs fycs tycs 123456'))
