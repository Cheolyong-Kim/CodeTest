#수정해야함

test_case_num=int(input()) #테스트 케이스 수 입력받기

for i in range(test_case_num): #테스트 케이스 수만큼 반복
    word_li=[] #입력한 단어들을 모아놓을 리스트
    ck=True #체크용 변수(팰린드롬이 있는지 없는지)
    word_num=int(input())  #단어 수 입력받기
    for j in range(word_num): #단어 수만큼 반복
        word_li.append(input()) #word_li에 저장
    for x in range(len(word_li)): #word_li의 길이만큼 반복
        for y in range(len(word_li)): #word_li의 길이만큼 반복
            if word_li[x]+word_li[y]==(word_li[x]+word_li[y])[::-1]: #word_li의 모든 원소끼리 합쳐서 팰린드롬인지 확인
                print(word_li[x]+word_li[y]) #팰린드롬이라면 출력
                ck=False #체크용 변수 False로
                break #하나만 출력하면 되기 때문에 break로 반복문 빠져나오기
    if ck: #팰린드롬이 없다면
        print(0)