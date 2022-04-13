# 코딩 테스트 연습문제 풀이 01

<br/>

1. [문제 링크(백준 알고리즘 문제 1000번)](https://www.acmicpc.net/problem/1000)

   ```python
   A,B=map(int,input().split())
   print(A+B)
   ```

<br/>

2. [문제 링크(백준 알고리즘 문제 2558번)](https://www.acmicpc.net/problem/2558)

   ```python
   A=int(input())
   B=int(input())
   print(A+B)
   ```

   <br/>

3. [문제 링크(백준 알고리즘 문제 10950번)](https://www.acmicpc.net/problem/10950)

   ```python
   n=int(input())
   for i in range(n):
       A,B=map(int,input().split())
       print(A+B)
   ```

   <br/>

4. [문제 링크(백준 알고리즘 문제 10953번)](https://www.acmicpc.net/problem/10953)

   ```python
   n=int(input())
   for i in range(n):
       A,B=map(int,input().split(','))
       print(A+B)
   ```

   <br/>

5. [문제 링크(백준 알고리즘 문제 11021번)](https://www.acmicpc.net/problem/11021)

   ```python
   n=int(input())
   for i in range(n):
       A,B=map(int,input().split())
       print(f"Case #{i+1}:",A+B)
   ```

   <br/>

6. [문제 링크(백준 알고리즘 문제 11022번)](https://www.acmicpc.net/problem/11022)

   ```python
   n=int(input())
   for i in range(n):
       A,B=map(int,input().split())
       print(f"Case #{i+1}: {A} + {B} =",A+B)
   ```

   <br/>

7. [문제 링크(백준 알고리즘 문제 2438번)](https://www.acmicpc.net/problem/2438)

   ```python
   N=int(input())
   for i in range(N):
       print('*'*(i+1))
   ```

   <br/>

8. [문제 링크(백준 알고리즘 문제 2439번)](https://www.acmicpc.net/problem/2439)

   ```python
   N=int(input())
   for i in range(1,N+1):
       print(' '*(N-i)+'*'*(i))
   ```

   <br/>

9. [문제 링크(백준 알고리즘 문제 10988번)](https://www.acmicpc.net/problem/10988)

   ```python
   word=input()
   if word==word[::-1]:
       print(1)
   else:
       print(0)
   ```

   <br/>

10. [문제 링크(백준 알고리즘 문제 2711번)](https://www.acmicpc.net/problem/2711)

    ```python
    N=int(input())
    for i in range(N):
        typo_idx,sentence=input().split()
        print(sentence[:int(typo_idx)-1]+sentence[int(typo_idx):])
    ```

    - 입력받은 오타 위치 인덱스를 활용하여 슬라이싱을 통해 간편하게 오타만 제외하고 출력한다.
    - 문제에서 오타는 반드시 1개라고 했으므로 슬라이싱 활용 가능

    <br/>

11. [문제링크(백준 알고리즘 문제 17249번)](https://www.acmicpc.net/problem/17249)

    ```python
    taebo=input()
    
    face=taebo.index('(')
    print(taebo[:face].count('@'),taebo[face:].count('@'))
    ```

    - 문제에서 필요한건 왼손@와 오른손@ 뿐이다.

    - 태보 이모티콘은 반드시 얼굴이모티콘(^0^)을 기준으로 양분되어있고 (^0^)에 사용하는 문자들은 (^0^)을 제외한 태보 이모티콘에서 사용하지 않기 때문에 (^0^)에 있는 아무 문자를 기준으로 태보 이모티콘을 양분한다.

    - 그 후 @의 수를 세서 출력한다.

      <br/>

12. [문제링크(백준 알고리즘 문제 2789번)](https://www.acmicpc.net/problem/2789)

    ```python
    censorship="CAMBRIDGE"
    
    word=input()
    for i in range(len(word)):
        if word[i] not in censorship:
            print(word[i],end='')
    ```

    - 입력한 word의 한 문자 한 문자가 censorship문자열에 있는지 확인하고 없다면 출력한다. 한 줄로 출력하기 위해서 end는 아무것도 없게 설정한다.

      <br/>

13. [문제링크(백준 알고리즘 문제 10995번)](https://www.acmicpc.net/problem/10995)

    ```python
    n=int(input())
    
    for i in range(1,n+1):
        if i%2!=0:
            print('* '*n)
        else:
            print(' *'*n)
    ```

    - 출력 규칙은
    - 우선, 입력한 수만큼의 행이 출력되고
    - 그 행이 홀수행이면 별 먼저 출력, 짝수행이면 공백먼저 출력한다.
    - 별의 개수는 입력한 수의 개수만큼 출력한다.

    <br/>

14. [문제링크(백준 알고리즘 문제 2675번)](https://www.acmicpc.net/problem/2675)

    ```python
    test_case_n=int(input()) #테스트 케이스 개수 입력 받기
    
    for num in range(test_case_n): #test_case_n만큼 반복
        r,s=input().split() #R,S 입력 받기
        for m in s: #S문자열에 있는 문자 하나하나 꺼내서 반복
                print(m*int(r),end='') #그 문자 하나를 r만큼 반복해서 출력, end는 아무것도 없이해서 이어지게 출력함
        if num!=test_case_n-1: #마지막 출력 때 개행하지 않도록 함
            print()
    ```

    - 문자열S에 있는 문자들을 하나씩 꺼내며 그 문자들을 R번 출력한다. 한 줄로 출력되게 하기 위해 end는 아무 값도 주지 않는다.
    - 한 문자열이 끝나면 개행되도록 반복문에 ``print()``를 넣어준다. 마지막 문자열에서는 개행되지 않게 조건문으로 걸러준다.

    <br/>

15. [문제링크(백준 알고리즘 문제 2941번)](https://www.acmicpc.net/problem/2941)

    ```python
    croatia_alphabet='c=','c-','dz=','d-','lj','nj','s=','z=' #크로아티아 알파벳 표기
    
    word=input() #입력 받기
    
    for ca in croatia_alphabet: #크로아티아 알파벳을 하나씩 꺼내며 반복
        if ca in word: #입력받은 word에 크로아티아 알파벳이 있다면
            word=word.replace(ca,'_') #_로 변환
    
    print(len(word)) #word문자열 길이 출력
    ```

    - 입력받은 문자열에서 크로아티아 알파벳을 '_'으로 변환한다. 
    - 변환된 word의 길이를 출력한다. 문제에서 입력되는 데이터는 알파벳 소문자와 '-', '='로만 이루어져있다고 했기 때문에 알고리즘에 문제가 생기지 않는다.
    - if문이 없어도 동작한다.