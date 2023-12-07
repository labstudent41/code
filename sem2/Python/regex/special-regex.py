import re

def title(text):
    print("\n\n\n"+ '='*3, text, '='*(68-len(text)), '\n')



title("Special Charecters")

x = "today is a pleasant day"
print(re.findall(r'\Atoday', x))
print(re.findall(r'ant\b', x))
print(re.findall(r'\Bday', x))
print(re.findall(r'day\d', x))
print(re.findall(r'\S', x))
print(re.findall(r'\s', x))
print(re.findall(r'day\D', x))
print(re.findall(r'\W', x))
print(re.findall(r'\w', x))
print(re.findall(r'\day\Z', x))




title("Sets")

x = "python PROGRAMMING is Case SENSitive 861423"
print(re.findall(r'[arn]', x))
print(re.findall(r'[a-n]', x))
print(re.findall(r'[^arn]', x))
print(re.findall(r'[0123]', x))
print(re.findall(r'[0-9]', x))
print(re.findall('[0-4][0-9]', x))
print(re.findall(r'[a-zA-Z]', x))




title('Search')

a = "happy new year"
x = re.search('new', a)
print('1st whitespace', x.start())
print(re.search('new', a))
print(re.search('year', a))

x = 'we all are Student'
a = re.search(r'\bS\w+', x)
print(a.span())
print(a.string)
print(a.group())




title('Split')

a = 'happy new year'
x = re.split('\s', a)
print(x)
print(re.split('\S', a, 1))




title('Sub')
a = 'we are doing python'
print(re.sub('\s', '9', a))
print(re.sub('\S', '9', a))
