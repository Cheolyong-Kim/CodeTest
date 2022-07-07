# 프로그래머스 Lv1 코드 풀이

<br/>

### 3진법 뒤집기

---

[3진법 뒤집기](https://programmers.co.kr/learn/courses/30/lessons/68935)

- 문제 설명

  1. 자연수 n -> 3진법 변환 -> 뒤집기

  2. 뒤집기한 3진법 수를 10진법으로 변환

     <br/>

- 제한사항

  1. n은 1 이상 100,000,000 이하인 자연수

     <br/>

- 코드

  ```python
  # 3진법 변환 후 뒤집기 함수
  def ternary_conversion_and_flip_over(l, n):
      if n < 3:
          l.append(int(n))
          return n
  
      a = int(n % 3)
      l.append(a)
  
      return ternary_conversion_and_flip_over(l, n / 3)
  
  # 3진법 -> 10진법 변환 함수
  def decimal_conversion(l):
      len_l = len(l)
      sum = 0
  
      for i in range(1, len_l + 1):
          sum += (l.pop() * (3 ** (i - 1)))
  
      return sum
  
  def solution(n):
      answer = 0
      l = []
      ternary_conversion_and_flip_over(l, n)
      answer = decimal_conversion(l)
  
      return answer
  ```

- 코드 풀이

  ```python
  # 3진법 변환 후 뒤집기 함수
  def ternary_conversion_and_flip_over(l, n):
      if n < 3:
          l.append(int(n))
          return n
  
      a = int(n % 3)
      l.append(a)
  
      return ternary_conversion_and_flip_over(l, n / 3)
  ```

  - 재귀함수 모양으로 구현
  - 매개변수로 리스트 l과 정수 n을 입력받는다
  - 재귀함수이기 때문에 우선 종료 조건을 설정. n보다 나눌 수가 작다면 리스트에 n을 추가하고 종료
  - n을 3으로 나눈 값을 정수형으로 형변환하고 l에 추가. 형변환하는 이유는 소수점 아래 자리들은 필요없기 때문
  - 함수동작이 끝나면 3진법으로 변환한 역순으로 리스트에 저장됨

  <br/>

  ```python
  # 3진법 -> 10진법 변환 함수
  def decimal_conversion(l):
      len_l = len(l)
      sum = 0
  
      for i in range(1, len_l + 1):
          sum += (l.pop() * (3 ** (i - 1)))
  
      return sum
  ```

  - 매개변수로 리스트 l을 받음
  - 1부터 리스트의 길이까지 반복
  - 내장함수 pop을 사용하여 리스트의 끝부분부터 3^(i - 1)해줌 (10진법 변환). 그 값을 sum에 누적합
  - sum을 반환

<br/>

---

### 신고 결과 받기

[신고 결과 받기](https://programmers.co.kr/learn/courses/30/lessons/92334)

- 문제 설명

  1. 유저 id 리스트, report 내역이 담긴 리스트, k 값이 입력으로 들어옴.
  2. 유저 id 리스트에는 유저들의 id가 담겨있음
  3. report 리스트에는 ["유저id 신고한id", ...] 으로 내용이 담겨 있음.
  4. k값은 정지 기준이 되는 신고 횟수
  5. k값 이상으로 신고당한 id는 정지당하고, 이 때 해당 id를 신고한 유저에게 메시지가 보내짐
  6. 각 유저당 받은 메시지 수를 출력함
  7. 각 유저는 한 번에 한 명의 유저를 신고할 수 있음
  8. 한 유저를 여러 번 신고할 수 있지만 동일한 유저에 대한 신고 횟수는 1회로 처리됨(중복 신고 불가능).

- 제한사항

  1. 2 <= id_list의 길이 <= 1000
     - 1 <= id_list의 원소 길이 <= 10
     - id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어짐
     - id_list에는 같은 아이디가 중복해서 들어있지 않음
  2. 1 <= report의 길이 <= 200,000
     - 3 <= report의 원소 길이 <= 21
     - id는 알파벳 소문자로만 이루어져 있음
     - 이용자id와 신고한id는 공백하나로 구분되어짐
     - 자기 자신을 신고하는 경우는 없음
  3. 1 <= k <= 200, k는 자연수
  4. return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 표현

- 코드

  ```python
  def solution(id_list, report, k):
      answer = [0 for _ in id_list]
      reported_dict = {id : 0 for id in id_list}
  
      for report_data in set(report):
          id, reported_id = report_data.split()
          reported_dict[reported_id] += 1
  
      for report_data in set(report):
          id, reported_id = report_data.split()
          if reported_dict[reported_id] >= k:
              answer[id_list.index(id)] += 1
  
      return answer
  ```

- 코드 풀이

  - 첫 코드가 시간제한으로 인해 테스트 통과 못함.
  - 1시간 고민해도 답이 안나와 다른 사람의 풀이를 참고

  ```python
  answer = [0 for _ in id_list]
  reported_dict = {id : 0 for id in id_list}
  ```

  - id_list의 유저 수만큼 answer를 0으로 초기화
  - id_list의 id를 키로 0을 벨류로 가지는 reported_dict 딕셔너리를 생성

  ```python
  for report_data in set(report):
      id, reported_id = report_data.split()
      reported_dict[reported_id] += 1
  ```

  - ``set(report)``로 중복된 값을 제거
  - ``set(report)``의 값들을 꺼내며 반복
  - report_data를 공백을 기준으로 split. 각각 id, reported_id 라고 변수 지정
  - reported_dict에 reported_id 키에 해당하는 벨류에 1을 더해줌
  - 각 유저별로 신고당한 내역을 저장하는 과정

  ```python
  for report_data in set(report):
      id, reported_id = report_data.split()
      if reported_dict[reported_id] >= k:
          answer[id_list.index(id)] += 1
  ```

  - if문 전까지 위 과정과 동일
  - reported_dict에 reported_id 키에 해당하는 벨류의 값이 k보다 크거나 같다면
  - answer의 인덱스에 1을 더함. id_list에서 현재 id와 같은 이름을 가진 인덱스를 찾아서 사용. 제한사항 4번이 존재하기 때문에 가능
  - 각 유저별로 받은 메시지 수를 계산하는 과정

<br/>

---

### 로또의 최고 순위와 최저 순위

[로또의 최고 순위와 최저 순위](https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3)

<br>

문제 간단 설명

-> 로또의 당첨 최고 순위와 최저 순위를 계산

-> 대신 입력으로 들어오는 lottos 리스트에 0이 포함되어 있음

-> 0은 어떤 숫자도 될 수 있음

-> 정해져있는 lottos의 로또 번호와 0을 포함해서 최고 순위와 최저 순위 정하기

<br>

코드

```python
def solution(lottos, win_nums):
    num_of_z = lottos.count(0)  # lottos의 0 개수를 세둠

    # lottos 원소가 전부 0이면
    if num_of_z == 6:
        top_ranking = 1
        lowest_ranking = 6
        answer = [top_ranking, lowest_ranking]
        return answer

    # lottos 원소가 전부 0이 아니면
    elif num_of_z == 0:
        set_lottos = set(lottos)
        set_win_nums = set(win_nums)
        dif_set = set_lottos - set_win_nums
        for i in dif_set:
            del lottos[lottos.index(i)]
        if len(lottos) == 0 or len(lottos) == 1:
            top_ranking = 6
            lowest_ranking = 6
            answer = [top_ranking, lowest_ranking]
            return answer
        else:
            top_ranking = 7 - len(lottos)
            lowest_ranking = 7 - len(lottos)
            answer = [top_ranking, lowest_ranking]
            return answer
    # 그 외
    else:
        lottos_ex_0 = list(set(lottos))
        lottos_ex_0.remove(0)

        set_lottos_ex_0 = set(lottos_ex_0)
        set_win_nums = set(win_nums)
        dif_set = set_lottos_ex_0 - set_win_nums
        for i in s:
            del lottos[lottos.index(i)]
        top_ranking = 7 - len(lottos)
        lowest_ranking = 7 - (len(lottos) - num_of_z)
        answer = [top_ranking, lowest_ranking]
        return answer
```

<br>

코드설명

문제 해결 방법의 순서를 먼저 설명

1. 0의 개수를 셈

2. 0이 6개면 최고 1등 최저 6등으로 정해져 있기 때문에 다른 작업 필요 X

3. 0이 0개이거나 그 외의 경우로 나눔

4. 0이 0개일 때

   4-1. 당첨번호와 중복된 번호가 0개 or 1개일 경우 무조건 6등

   4-2. 그 외의 경우 (7 - 맞춘 번호 수)등

5. 그 외

   5-1. 최고 순위는 (7 - 0을 포함한 맞춘 번호 수)등

   5-2. 최저 순위는 (7 - 맞춘 번호 수 - 0의 개수)등

위 해결 방법을 코드로 구현

<br>

set을 활용하여 0을 쉽게 제거할 수 있게 하고

집합 연산을 통해 당첨 번호가 아닌 것을 쉽게 계산할 수 있게 만듦.

<br>

---

