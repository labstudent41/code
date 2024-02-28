import re

print(re.split(r'\s*', 'The first regular expression'))
print(re.split(r'[a-e]', 'Advance python programming'))

print('\nfind the digits')
print(re.findall(r'\d', 'Roll no. of David is 51236 & marks is 9.999'))

print('\nfind the non-digits')
print(re.findall(r'\D', 'Roll no. of David is 51236 & marks is 9.999'))

print('\nfind the non-space')
print(re.findall(r'\S', 'Roll no. of David is 51236 & marks is 9.999'))




a = 'today is gown day and western day in vartak college'
print('\n\n')
print(re.findall(r'\d', a))
print(re.findall(r'.', a))
print(re.findall(r'/', a))
print(re.findall(r'^today', a))
print(re.findall(r'college$', a))
print(re.findall(r'and$', a))
print(re.findall(r'..d', a))
print(re.findall(r'v.r..k', a))
print(re.findall(r'.*y', a))
print(re.findall(r'.+y', a))
print(re.findall(r'co.{2}', a))
print(re.findall(r'gown|hello', a))
print(re.findall(r'gown|in', a))

