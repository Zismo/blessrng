#k=x=1
#x=1
#lol = 'программа'

#print(f'{x} {k} {lol}', end=';\n')
#print('{0}\n{1}'.format(x, k))

#k=-2

#if k>0:
#    print('Hello world!')

#elif k<0:
#    print('k<0')
#else:
#    print('k=0')

#arr = [1,2,3]

#for item in arr:
#    print(item, end=' ')
#    print()

 #   for item2 in range(len(arr)):
#        print(item2, end=' ')

#print()

#for i in range(len(arr)):
 #   print(i, end=' ')
#j=0

#while j<10:
#    j +=1
#    print(j, end=' ')

#def add(a: int, b: int):
#    if not(isinstance(a, int)) or not(isinstance(b, int)):
#        print('not int')
#        return None
#    return a + b

#print(add(1, 2))
#print(add('123','12'))

#a = {} - Словарь

#a[123] = 'Artem'
#a[1] = 'Ilya'

#print(a[123])

#b = {
#    '123': 'Artem'
#    '546': 'fsgsgsdgsdg'
#}

#print(a)
#print(b)

#a = []

#a.append(1)
#a.append(2)

#b=[4, 34, 9]

#def foo():
#    print('xm xm xm.. I am doing something')

#def getNewFoo(f):
#    def decorator():
#        print('Hello world!')
#        f()
#        print('end')
#    return decorator

#if _name_ == '_main_'


#class MyClass(object):
#    def __init__(self, number: int):
#        self.number = number
#        self._number = number + 1
#        self.__number = number + 2

#    def add(self, number2: int) -> int:
#        return self.number + number2

#    def __str__(self):
#        return 'kek'


#a = MyClass(1)
#a.MyClass__number
#b = MyClass(2)
#print(str(a))


#print('Enter name of file: ', end=' ')
#nameFile = input()

#try:
#    file = open(nameFile, 'r')
#except IOError as error:
#    print(str(error))
#else:
#    with file:
#        for line in file:
#            print(line, end=' ')
#    print()
#    print(f'file is closed: {file.closed}')