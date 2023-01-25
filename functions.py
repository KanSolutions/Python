def sayHi(name , age):
    print('hello User! ' + name  + ' age is '+ str(age) )
sayHi('v',25)

def cube(num):
    return num*num*num

print(cube(3))
result = cube(4)
print(result)

# If statements

# if condition:
    # body of if statement

number = 60
if number > 20:
    print("condition is True")
else:
    print("consition is False")

# if ...elif..else

if number < 50:
    print("passed first if")
elif number < 65:
    print("passsed ... elif")
else:
    print("condition is false")

# or .. and ..not
is_male = True
is_female = False
if is_male and is_female:
    print('u r a female')
elif is_male or not(is_female):
    print('not test')
else:
    print("u r not a female")
# statements with comparison operators

def max_number(num1, num2 , num3 ):
    if num1 >= num2 and num2 >= num3:
        return num1
    elif num2>= num1 or num2 >=num3:
        return num2
    else:
        return num3

print(max_number(10, 30, 5))

# calsi
data_1 = float(input("Enter the first num: "))
op = input("Enter the op: ")
data_2 = float(input("Enter second num : ") )

if op == "+":
    print(data_1 + data_2)
elif op == "-" :
    print(data_1 - data_2)
elif op == "/":
    print(data_1 / data_2)
elif op == "*":
    print(data_1 * data_2)
else:
    "invalid op"





