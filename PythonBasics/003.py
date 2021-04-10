#! Python Tuples



## Create and print tuples

print('## Create and print tuples');
print('\n')
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1[3])
print(tup2[1:4])

print('\n')

print('##Tuple packing and unpacking')
print('\n')
x = ("Mahir Ahmed", 27, "Developer")    # tuple packing
(name, emp, profile) = x    # tuple unpacking
print(name)
print(emp)
print(profile)

print('\n')

## Comparing Tuples 

print('## Comparing Tuples');

print('\n')
a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

## Using tuples as keys in dictionaries

print ('##Using tuples as keys in dictionaries')
print('\n')
a = {'x':100, 'y':200}
b = a.items()
print (b)
