# 코딩 테스트 연습 문제 풀이 03

<br/>

1. [문제 링크(정올 문제 945번)](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4372&sca=pyd0)

   ```python
   animation = {
       "Pokemon" : "Pikachu",
       "Digimon" : "Agumon",
       "Yugioh" : "Black Magician"
       }
   
   name = input()
   
   print(animation.get(name) if animation.get(name) else "I don't know")
   ```

   <br/>

   <br/>

2. [문제 링크(정올 문제 946번)](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4373&sca=pyd0)

   ```python
   n = int(input())
   
   capital_dic = {}
   for i in range(n):
       country, capital = input().split()
       capital_dic[country]=capital
   
   find_capital=input()
   print(capital_dic[find_capital] if capital_dic.get(find_capital) else 'Unknown Country')
   ```

   <br/>

   <br/>

3. [문제 링크(정올 문제 953번)](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4380&sca=pyd0)

   ```python
   f_records = input().split()
   
   players = {
       "Jay" : 0,
       "John" : 0,
       "Jack" : 0,
       "Jo" : 0
   }
   
   for f_record in f_records:
       players[f_record] += 1
   
   min_foul = min(players.values())
   for player, foul in players.items():
       if foul == min_foul:
           print(player)
   print(min_foul)
   ```

   <br/>

   <br/>

4. [문제 링크(백준 알고리즘 1764번)](https://www.acmicpc.net/problem/1764)

   ```python
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
   ```

   - 이 문제에서 굳이 '듣도 못한 사람', '보도 못한 사람'으로 나눌 필요가 없다.
   - 빈 딕셔너리를 하나 만들어 놓는다.
   - 입력된 이름이 딕셔너리에 없다면 그 이름을 키값으로 키-값쌍을 만든다.
   - 입력된 이름이 이미 존재한다면 그 키의 값을 1로 바꿔준다.
   - 딕셔너리에서 값이 1인 키들은 모두 듣도, 보도 못한 사람이기 때문에(입력이 두번됨)
   - 값이 1인 키의 수와 키들을 출력하면 된다.

   <br/>

   <br/>

5. [문제 링크(백준 알고리즘 문제 5622번)](https://www.acmicpc.net/problem/5622)

   ```python
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
   ```

   <br/>

   <br/>

6. [문제 링크(백준 알고리즘 문제 16165번)](https://www.acmicpc.net/problem/16165)

   ```python
   N, M = map(int, input().split())
   
   team_dic = {}
   for i in range(N + M):
       #걸그룹 초기화 부분
       if i <= N-1:
           team_list = []
           team_name = input()
           mem_num = int(input())
           for _ in range(mem_num):
               mem = input()
               team_list.append(mem)
           team_dic[team_name] = sorted(team_list)
       #퀴즈 부분
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
   ```

   <br/>

   <br/>

7. [문제 링크(백준 알고리즘 문제 1620번)](https://www.acmicpc.net/problem/1620)

   ```python
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
   ```

   - 계속 시간초과로 나와서 어떻게든 시간을 줄였다.
   - input() 대신 sys.stdin.readline()을 사용했고 중첩 반복들을 모두 제거했다.

   <br/>

   <br/>

8. [2021 카카오 채용 연계 인턴 코딩테스트 기출문제 : 숫자 문자열과 영단어](https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3)

   ```python
   converse_dic = {
       'zero': 0,
       'one': 1,
       'two': 2,
       'three': 3,
       'four': 4,
       'five': 5,
       'six': 6,
       'seven': 7,
       'eight': 8,
       'nine': 9
   }
   
   def solution(s):
       text=s
       for eng, num in converse_dic.items():
           if eng in text:
               text = text.replace(eng, str(num))
               print(eng)
   
       answer = text
       return answer

