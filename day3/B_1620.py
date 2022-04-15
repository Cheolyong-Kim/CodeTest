import sys

# poke_num, quiz_num = map(int, input().split())
poke_num, quiz_num = [int(x) for x in sys.stdin.readline().split()]
            
poke_dic = {}
reverse_poke_dic = {}
#도감 입력 부분
for n in range(poke_num):
    # poke_name = input()
    poke_name = sys.stdin.readline().strip()
    poke_dic[n + 1] = poke_name
    reverse_poke_dic[poke_name] = n + 1

#퀴즈 부분
for m in range(quiz_num):
    # quiz = input()
    quiz = sys.stdin.readline().strip()
    if quiz.isdigit():
        print(poke_dic[int(quiz)])
    else:
        print(reverse_poke_dic[quiz])