import numpy as np

def init_li():
    array=np.array([list(map(int,input().split())), list(map(int,input().split()))])
    return array

for i in range(2):
    if i == 0:
        print('first array')
        first_array = init_li()
    else:
        print('second array')
        second_array = init_li()

array_mul = first_array * second_array

#출력결과를 문제와 동일하게 하기 위해 배열의 각 원소를 꺼내서 보여줌
for i in range(2):
    for j in range(3):
        print(array_mul[i][j], end=' ')
    print()