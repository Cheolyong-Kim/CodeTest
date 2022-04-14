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