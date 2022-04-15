N, M = map(int, input().split())

team_dic = {}
for i in range(N + M):
    if i <= N-1:
        team_list = []
        team_name = input()
        mem_num = int(input())
        for _ in range(mem_num):
            mem = input()
            team_list.append(mem)
        team_dic[team_name] = sorted(team_list)
    else:
        name = input()
        quiz = int(input())
        if quiz == 1:
            for team, mem in team_dic.items():
                if name in mem:
                    print(team)
        else:
            for name in team_dic[name]:
                print(name)
