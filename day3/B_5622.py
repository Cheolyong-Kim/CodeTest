dial_dic = {
    'ABC': 2,
    'DEF': 3,
    'GHI': 4,
    'JKL': 5,
    'MNO': 6,
    'PQRS': 7,
    'TUV': 8,
    'WXYZ': 9
}

alpha_list = list(input())

sum = 0
for dial_key, num in dial_dic.items():
    for alphabet in alpha_list:
        if alphabet in dial_key:
            sum += num + 1

print(sum)