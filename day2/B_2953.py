score_list = []

for i in range(5):
    score_list.append(sum(list(map(int,input().split()))))

max = max(score_list)
participation_number = score_list.index(max)+1

print(participation_number, max)