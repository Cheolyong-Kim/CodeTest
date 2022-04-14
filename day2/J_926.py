import numpy as np

def init_li(array):
    array=np.array([list(map(int,input().split())), list(map(int,input().split()))])
    return array

first_array = init_li(input())
second_array = init_li(input())
array_mul = first_array * second_array

#출력결과를 문제와 동일하게 하기 위해 배열의 각 원소를 꺼내서 보여줌
for i in range(2):
    for j in range(4):
        print(array_mul[i][j], end=' ')
    print()