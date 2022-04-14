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

