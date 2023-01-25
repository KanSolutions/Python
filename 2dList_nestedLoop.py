number_grids = [
    [1,5,8],
    [2, 9, 6],
    [4, 3],
    [0]
]
print(number_grids[2][0])

for row in number_grids:
    for item in row:
        print(item)


def trans(str):
    tn = ""
    for lnt in str:
        if lnt.lower() in 'aieou':
            if lnt.isupper():
                tn = tn+ "g"
            else:
                tn = tn + "G"
        else:
            tn = tn + lnt
    return tn

print(trans(input("enter a ip : ")))

#comments
#
'''
abc
def
ghi
'''



