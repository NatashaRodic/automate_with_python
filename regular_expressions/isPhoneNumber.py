import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print(isPhoneNumber('123-123-1234')) 
phoneNumRegex = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415)555-4242')
print('Phone number found: ' + mo.group())


## Grouping with parentheses
print(mo.group(1)) #415
print(mo.group(2)) #555-4242
print(mo.group(0)) #415-555-4242
print(mo.groups())  #('415', '555-4242')

areaCode, mainNumber = mo.groups()  #Using multiple assignment trick to assign each value to separate variable
print(areaCode)
print(mainNumber)

#One or more: Repetitions with Braces

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None

haRegex = re.compile(r'(Ha){3}') #Will match the string with 3 repetitions of ha: We can also do (Ha){3,} -> 3 or more; (Ha){,5} -> 0 to five instances
mo4 = haRegex.search('HaHaHa')
print(mo4.group())


