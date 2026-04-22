class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cs = [set() for _ in range(len(board))]
        rs = [set() for _ in range(len(board))]
        ss = [set() for _ in range(len(board))]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                #column
                if board[r][c] in cs[c]:
                    return False             
                cs[c].add(board[r][c])
                
                #row
                if board[r][c] in rs[r]:
                    return False
                rs[r].add(board[r][c])
                
                #sector
                #sector 1
                if c <= 2 and r <= 2:
                    if board[r][c] in ss[0]:
                        return False
                    else:
                        ss[0].add(board[r][c])
                #sector 2
                if c >= 3 and c <= 5 and r <= 2:
                    if board[r][c] in ss[1]:
                        return False
                    else:
                        ss[1].add(board[r][c])
                #sector 3
                if c >= 6 and r <= 2:
                    if board[r][c] in ss[2]:
                        return False
                    else:
                        ss[2].add(board[r][c])
                #sector 4
                if c <= 2 and r >= 3 and r <= 5:
                    if board[r][c] in ss[3]:
                        return False
                    else:
                        ss[3].add(board[r][c])
                #sector 5
                if c >= 3 and r >= 3 and c <= 5 and r <= 5:
                    if board[r][c] in ss[4]:
                        return False
                    else:
                        ss[4].add(board[r][c])
                #sector 6
                if r >= 3 and r <= 5 and c >= 6:
                    if board[r][c] in ss[5]:
                        return False
                    else:
                        ss[5].add(board[r][c])
                #sector 7
                if c <= 2 and r >= 6:
                    if board[r][c] in ss[6]:
                        return False
                    else:
                        ss[6].add(board[r][c])
                #sector 8
                if c <= 5 and c >= 3  and r >= 6:
                    if board[r][c] in ss[7]:
                        return False
                    else:
                        ss[7].add(board[r][c])
                #sector 9
                if c >= 6 and r >= 6:
                    if board[r][c] in ss[8]:
                        return False
                    else:
                        ss[8].add(board[r][c])
        return True
