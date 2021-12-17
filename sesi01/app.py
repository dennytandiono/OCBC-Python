
print("===Float===")
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

print("===Strings===")
print("Hacktiv8")
print(type("Hacktiv8"))
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')


print("===Python 3 provides a Boolean data type. Objects of Boolean type may have one of two values, True or False:")
print(type(True))
print(type(False))

print("===When you compare two values, the expression is evaluated and Python returns the Boolean answer:")
print(100 > 200) #False
print(100 == 200) #False
print(100 < 200) #True


print("===Variable Assignment===")
n = 300
print(n)

print("===Chained Type assignment===")
a = b = c = 300
print(a, b, c)


print("===Variable Names===")
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)


print("===Operators and Expressions===")
a = 10
b = 20
print(a + b)
print(a + b - 5)


print("===Arithmetic Operators===")
a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b) # (**) = pangkat


print("===Comparison Operators===")
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)


print("===String Manipulation===")
s = 'foo'
t = 'bar'


print(s + t)
print(s * 4)


print(s.capitalize())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.upper())

a = ['foo', 'bar', 'baz', 'qux']

print(a)

a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']

a == b

a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0])
print(a[5])
print(a[-1])
print(a[-6])

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print (a[2:5])


print(a)

print(a + ['grault', 'garply'])
print(a * 2)

print(a)

print(len(a))
print(min(a))
print(max(a))

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a)

a[2] = 10
a[-1] = 20

print(a)


del a[3]
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[1:4])

a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]

print(a)

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

print(t)
print(t[0])

print(t[-1])

(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')

print(s1)

MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}
print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])


MLB_team['Kansas City'] = 'Royals'
MLB_team

MLB_team['Seattle'] = 'Seahawks'
MLB_team

del MLB_team['Seattle']


person = {}
type(person)
 
person['fname'] = 'Hack'
person['lname'] = 'Inalum'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

print(person['fname'])
print(person['lname'])
print(person['children'])
print(person['children'][1])
print(person['pets'])
print(person['pets']['cat'])


d = {'a': 10, 'b': 20, 'c': 30}

print(d.items())

print(d.keys())

print(d.values())

print('Hello, World!')

x = [1, 2, 3]
print(x)
