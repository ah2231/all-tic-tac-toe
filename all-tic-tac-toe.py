def isWin(board, n):
    if board[0] == n and board[1] == n and board[2] == n: return 1
    if board[3] == n and board[4] == n and board[5] == n: return 1
    if board[6] == n and board[7] == n and board[8] == n: return 1

    if board[0] == n and board[3] == n and board[6] == n: return 1
    if board[1] == n and board[4] == n and board[7] == n: return 1
    if board[2] == n and board[5] == n and board[8] == n: return 1
    
    if board[0] == n and board[4] == n and board[8] == n: return 1
    if board[2] == n and board[4] == n and board[6] == n: return 1
    return 0

pieces = ['', 'x', 'o']
board = [0] * 9
count = 0

for board[0] in range (3):
    for board[1] in range (3):        
        for board[2] in range (3):
            for board[3] in range (3):
                for board[4] in range (3):
                    for board[5] in range (3):
                        for board[6] in range (3):
                            for board[7] in range (3):
                                for board[8] in range (3):
                                    countX = sum([1 for x in board if x == 1])
                                    countO = sum([1 for x in board if x == 2])

                                    if abs(countX - countO) < 2:
                                        if isWin(board, 1) + isWin(board, 2) == 1:
                                            count += 1
                                            print " %s | %s | %s" % (pieces[board[0]],pieces[board[1]],pieces[board[2]])
                                            print "---+---+---"
                                            print " %s | %s | %s" % (pieces[board[3]],pieces[board[4]],pieces[board[5]])
                                            print "---+---+---"
                                            print " %s | %s | %s" % (pieces[board[6]],pieces[board[7]],pieces[board[8]])
                                            print

print count                                            