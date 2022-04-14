num_list = list(map(int, input().split()))

def print_list(list):
    for num in list:
        print(num, end=' ')
    print()

n = 0
run = True
while run:
    i = n % 4
    if num_list[i] > num_list[i + 1]:
        tmp = num_list[i + 1]
        num_list[i + 1] = num_list[i]
        num_list[i] = tmp
        n += 1
        print_list(num_list)
    else:
        n += 1
        continue

    if [1, 2, 3, 4, 5] == num_list:
        run = False

