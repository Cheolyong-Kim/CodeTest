N, M = map(int, input().split())

dbj_dic = {}
for i in range(N + M):
    name = input()
    if dbj_dic.get(name) == None:
        dbj_dic[name] = 0
    else:
        dbj_dic[name] = 1

count = 0
dbj_list = []
for name, value in dbj_dic.items():
    if value == 1:
        dbj_list.append(name)
        count += 1

print(count)
for name in sorted(dbj_list):
    print(name)