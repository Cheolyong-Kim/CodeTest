censorship="CAMBRIDGE"

word=input()
for i in range(len(word)):
    if word[i] not in censorship:
        print(word[i],end='')