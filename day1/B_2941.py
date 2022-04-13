croatia_alphabet='c=','c-','dz=','d-','lj','nj','s=','z=' #크로아티아 알파벳 표기

word=input() #입력 받기

for ca in croatia_alphabet: #크로아티아 알파벳을 하나씩 꺼내며 반복
    if ca in word: #입력받은 word에 크로아티아 알파벳이 있다면
        word=word.replace(ca,'_') #_로 변환

print(len(word)) #word문자열 길이 출력

