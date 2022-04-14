N = int(input())
num_list = [0 for _ in range(N)]

for i in range(N):
    num_list[i] = int(input())

num_list.sort()
for num in num_list:
    print(num)