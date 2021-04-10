#! Python arrays

print('#! Python arrays')

print('\nPrinting array')
cars = ["Ford", "Volvo", "BMW"]
print(cars)

print('\nRevesing array')
cars = ["Ford", "Volvo", "BMW"]
cars.reverse()
print(cars)

print('\nLength of array')
print(len(cars))

print('\nLooping array')
for x in cars:
    print(x)

print('\nAppending to array and print')
cars.append('Ferrari')
print(cars)

print('\nPopping from array and print')
cars.pop(2)
print(cars)

print('\nRemoving from array and print')
cars.remove('Volvo')
print(cars)