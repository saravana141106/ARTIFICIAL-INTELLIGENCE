N = 8
board = [-1] * N

def solve(r):
    if r == N:
        print(board)
        return True

    for c in range(N):
        ok = True
        for i in range(r):
            if board[i] == c or abs(board[i] - c) == abs(i - r):
                ok = False
                break

        if ok:
            board[r] = c
            if solve(r + 1):
                return True

    return False

solve(0)
