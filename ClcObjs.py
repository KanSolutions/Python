# class ClcObjs:
#
#     def student(self):
import random
import secrets
import string

print(random.random())

print(random.randint(6, 9))

val=[3,7,9,0]
print(random.choice(val))
print(random.sample(val, k=3))
print('secrete module')
print(secrets.choice(val), )
alpha = string.ascii_letters

print(alpha)
print([secrets.choice(alpha) for i in range(10)])
print(secrets.randbelow(8))

#decimal module