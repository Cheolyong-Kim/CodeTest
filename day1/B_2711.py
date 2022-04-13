N=int(input())
for i in range(N):
    typo_idx,sentence=input().split()
    print(sentence[:int(typo_idx)-1]+sentence[int(typo_idx):])