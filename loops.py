# i=1
# while i <= 10:
#     print(i)
#     i += 2


#len(data)
lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

# print(len(lst))
i=0
while i < len(lst):
    if lst[i] == 100:
        print(str(i))
    i = i + 1
# for loop
for letter in "America":
    print(letter)

city =['bng', 'mys', 'mang']
for ci_ty in city:
    print(ci_ty)


for index in range(10):
    print(index)
print("\n")
for index in range(3, 7):
    print(index)

print("#########################")
for index in range(2):
    print(index)

def power_to(base_num,pow):
    result=1
    for index in range(pow):
        result = result * base_num
    return result

print(power_to(3,2))