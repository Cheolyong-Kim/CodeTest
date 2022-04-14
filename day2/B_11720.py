N = int(input())
num = input()

num_list = [0 for _ in range(N)]

for i in range(N):
    num_list[i] = int(list(num)[i])

print(sum(num_list))