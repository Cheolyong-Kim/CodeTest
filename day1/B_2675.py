test_case_n=int(input()) #테스트 케이스 개수 입력 받기

for num in range(test_case_n): #test_case_n만큼 반복
    r,s=input().split() #R,S 입력 받기
    for m in s: #S문자열에 있는 문자 하나하나 꺼내서 반복
            print(m*int(r),end='') #그 문자 하나를 r만큼 반복해서 출력, end는 아무것도 없이해서 이어지게 출력함
    if num!=test_case_n-1: #마지막 출력 때 개행하게 하지 않도록 함
        print()