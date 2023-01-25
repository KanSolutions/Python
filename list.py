# Lists are used to store multiple items in a single variable.

alpha = ['a', 'B', 'c', 8, True]

print(alpha)
print(alpha[0])
print(alpha[-2])
print(alpha[1:3])

alpha[0] = "A"
print(alpha[0])
#List functions
numeric =['1', '2','3']
numeric.extend(alpha)
print(numeric)
#
numeric.append('number_values')
print(numeric)
#
numeric.insert(0, "one")
print(numeric)
#
numeric.remove("2")
print(numeric)
#
numeric.append("one")

print(numeric.count('one'))
#
frnds = ['neow', 'paint', 'color']
frnds.sort()
print(frnds)
#
numeric_values =['10', '29','3']
numeric_values.reverse()

print(numeric_values)
#
numbers2 = numeric_values.copy()
print(numbers2)