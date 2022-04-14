# 코딩 테스트 연습문제 풀이 02

<br/>

1. [문제 링크(백준 알고리즘 문제 11720번)](https://www.acmicpc.net/problem/11720)

   ```python
   N = int(input())
   num = input()
   
   num_list = [0 for _ in range(N)]
   
   for i in range(N):
       num_list[i] = int(list(num)[i])
   
   print(sum(num_list))
   ```

   - num_list를 N칸으로 초기화해줬는데 굳이 하지 않아도 된다.

   - 파이썬의 경우 처음 입력을 입력만 받고 사용하지 않은 상태에서 진행해도 답이 나온다.

     ```python
     _ = input()
     
     print(sum(map(int, list(input()))))
     ```

   <br/>

2. [문제 링크(백준 알고리즘 문제 2750번)](https://www.acmicpc.net/problem/2750)

   ```python
   N = int(input())
   num_list = [0 for _ in range(N)]
   
   for i in range(N):
       num_list[i] = int(input())
   
   num_list.sort()
   for num in num_list:
       print(num)
   ```

   - 위 문제와 마찬가지로 굳이 num_list를 초기화하지 않아도 된다.

     ```python
     N = int(input())
     
     num_list = [int(input()) for i in range(N)]
     
     for num in sorted(num_list):
         print(num)
     ```

   <br/>

3. [문제 링크(정올 문제 921번)](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4348&sca=pyc0)

   ```python
   n = int(input())
   squared_list = [i**2 for i in range(1,n+1)]
   print(squared_list)
   ```

   <br/>

4. [문제 링크(정올 문제 929번)](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4356&sca=pyc0)

   ```python
   n = int(input())
   squared_list = [f"No.{i}" for i in range(1,n+1)]
   print(squared_list)
   ```

   <br/>

5. [문제 링크(백준 알고리즘 문제 2562번)](https://www.acmicpc.net/problem/2562)

   ```python
   num_list = [int(input()) for i in range(9)]
   
   max_num = max(num_list)
   print(max_num)
   print(num_list.index(max_num)+1)
   ```

   <br/>

6. [문제 링크(정올 문제 926번)](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4353&sca=pyc0)

   ```python
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
   ```

   - 파이썬 라이브러리 넘파이를 사용해서 간편하게 풀었다

   <br/>

7. [문제 링크(정올 문제 937번)](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4364&sca=pyc0)

   ```python
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
   ```

   - 위 문제와 크게 다르지 않다

   <br/>

8. [문제 링크(백준 알고리즘 문제 1100번)](https://www.acmicpc.net/problem/1100)

   ```python
   chess_board = []
   
   for i in range(8):
       chess_board.append(list(input()))
   
   chess_on_whie_board=0
   for i in range(len(chess_board)):
       #짝수번째 행에는 짝수번째 열이 흰색 칸. 그 곳에 F가 있는지 확인
       if i % 2 == 0:
           for j in range(len(chess_board[i])):
               if j % 2 == 0:
                   if chess_board[i][j] == 'F':
                       chess_on_whie_board += 1
       #홀수번째 행에는 홀수번째 열이 흰색 칸. 그 곳에 F가 있는지 확인
       else:
           for j in range(len(chess_board[i])):
               if j % 2 != 0:
                   if chess_board[i][j] == 'F':
                       chess_on_whie_board += 1
   
   print(chess_on_whie_board)
   ```

   - 위 코드를 더 간단하게 줄일 수 있다.

     ```python
     chess_board = []
     
     for i in range(8):
         chess_board.append(list(input()))
     
     chess_on_whie_board=0
     for i in range(8):
         for j in range(8):
             #하얀 칸은 짝수행+짝수열이거나 홀수행+홀수열이다.
             if i % 2 == j % 2 and chess_board[i][j] == 'F':
                 chess_on_whie_board += 1
     
     print(chess_on_whie_board)
     ```

   <br/>

9. [문제 링크(백준 알고리즘 문제 2953번)](https://www.acmicpc.net/problem/2953)

   ```python
   score_list = []
   
   for i in range(5):
       score_list.append(sum(list(map(int, input().split()))))
   
   max = max(score_list)
   participation_number = score_list.index(max)+1
   
   print(participation_number, max)
   ```

   <br/>

10. [문제 링크(백준 알고리즘 문제 4344번)](https://www.acmicpc.net/problem/4344)

    ```python
    testcase_num = int(input())
    
    def avg(list):
        avg_num = sum(list[1:]) / list[0]
        return avg_num
    
    for i in range(testcase_num):
        score_list = list(map(int, input().split()))
        score_over_avg = [score for score in score_list[1:] if score > avg(score_list)]
        ratio_of_student_over_avg = (len(score_over_avg) / score_list[0]) * 100
        print(f"{ratio_of_student_over_avg:.03f}%")
    ```

    - 평균 구하는 함수를 굳이 구축하지 않아도 된다.

    <br/>

11. [문제 링크(백준 알고리즘 문제 2947번)](https://www.acmicpc.net/problem/2947)

    ```python
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
    ```

    - 이 알고리즘보다 버블정렬알고리즘을 사용하는게 훨씬 좋을 것이다.

    <br/>

12. [문제 링크(백준 알고리즘 2563번)](https://www.acmicpc.net/problem/2563)

    ```python
    drawing_paper = [[0] * 100 for _ in range(100)]
    confetti_num = int(input())
    
    #drawing_paper에서 (입력한 x좌표)(입력한 y좌표)~(입력한 x좌표+10)(입력한 y좌표+10)까지 모두 1로 채워준다.
    for i in range(confetti_num):
        x, y = map(int,input().split())
        for row in range(x-1, x+9):
            for col in range(y-1, y+9):
                drawing_paper[row][col] = 1
    
    #drawing_paper에서 0이 아닌 1의 개수를 세면 drawing_paper에서 색종이가 차지하는 넓이를 구할 수 있다.
    count = 0
    for x in range(100):
        for y in range(100):
            if drawing_paper[x][y] == 1:
                count += 1
    
    print(count)
    ```

    - (색종이 넓이 - 겹치는 부분)으로 구현하려하면 복잡해서 잘 되지 않는다.
    - 겹치는 부분이라고 생각하지 말고 칠해져있는 부분이라고 생각한 뒤
    - 칠해진 부분의 넓이만 구하면 된다.
    - 100x100칸의 0으로 초기화된 리스트를 준비한다.
    - 입력된 좌표에서 10x10 크기로 1을 채운다.
    - 리스트에서 1의 개수를 세면 답이 나온다. 