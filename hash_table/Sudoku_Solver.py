# Question No.34 Sudoku Solver
import copy


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Mine Solution , not work
        # rows = {}
        # columns = {}
        # blocks = {}
        # uncheck = []
        # # init sudoku board data structure
        # for i in range(3):
        #     for k in range(3):
        #         for j in range(3):
        #             for w in range(3):
        #                 row_num = i * 3 + k
        #                 column_num = j * 3 + w
        #                 block_num = i * 3 + j
        #                 num = su((board[row_num][column_num]), row_num, column_num, block_num)
        #
        #                 if num.val == '.':
        #                     uncheck.append(num)
        #                 else:
        #                     num.val = (int)(num.val)
        #                     if row_num in rows.keys():
        #                         rows[row_num].append(num)
        #                     else:
        #                         rows[row_num] = [num]
        #                     if column_num in columns.keys():
        #                         columns[column_num].append(num)
        #                     else:
        #                         columns[column_num] = [num]
        #                     if block_num in blocks:
        #                         blocks[block_num].append(num)
        #                     else:
        #                         blocks[block_num] = [num]
        #
        # for i in range(9):
        #     if not i in rows.keys():
        #         rows[i] = []
        #     if not i in columns.keys():
        #         columns[i] = []
        #     if not i in blocks.keys():
        #         blocks[i] = []
        #
        # while len(uncheck) > 0:
        #     for i in range(len(uncheck) - 1, -1, -1):
        #         num = uncheck[i]
        #         nine = list(range(1, 10, 1))
        #         for k in rows[num.row]:
        #             if k.val in nine:
        #                 nine.remove(k.val)
        #         for k in columns[num.column]:
        #             if k.val in nine:
        #                 nine.remove(k.val)
        #         for k in blocks[num.block]:
        #             if k.val in nine:
        #                 nine.remove(k.val)
        #         if len(nine) == 1:
        #             num.val = nine[0]
        #             uncheck.remove(num)
        #
        # for i in range(9):
        #     for j in range(9):
        #         board[i][j] = rows[i][j].val


        # class su:
        #     def __init__(self, x, row, column, block):
        #         self.val = x
        #         self.row = row
        #         self.column = column
        #         self.block = block

        cells = [[cell() for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and not self.setCell(i, j, ord(board[i][j]) - ord('0'), cells):
                    return

        if not self.findValuesForEmptyCells(cells):
            return

        for i in range(9):
            for j in range(9):
                if cells[i][j].val:
                    board[i][j] = str(cells[i][j].val)
        return

    def setCell(self, i, j, v, cells):
        c = cells[i][j]
        if c.val == v:
            return True
        if c.notPossible[v]:
            return False
        c.notPossible = [1] * 10
        c.notPossible[v] = 0
        c.numPossibilities = 1
        c.val = v

        for k in range(9):
            if i != k and not self.updateConstraints(k, j, v, cells):
                return False
            if j != k and not self.updateConstraints(i, k, v, cells):
                return False
            ix = i // 3 * 3 + k // 3
            jx = j // 3 * 3 + k % 3
            if ix != i and jx != j and not self.updateConstraints(ix, jx, v, cells):
                return False
        return True

    def updateConstraints(self, i, j, excludedValue, cells):
        c = cells[i][j]
        if c.notPossible[excludedValue]:
            return True
        if c.val == excludedValue:
            return False

        c.notPossible[excludedValue] = True
        if --c.numPossibilities > 1:
            return True

        for v in range(1, 10):
            if not c.notPossible[v]:
                return self.setCell(i, j, v, cells)
        return False

    def findValuesForEmptyCells(self, cells):
        emptyCells = []
        for i in range(9):
            for j in range(9):
                if not cells[i][j].val:
                    emptyCells.append((i, j))
        emptyCells.sort(key=lambda tup: cells[tup[0]][tup[1]].numPossibilities)
        return self.solveBacktrack(0, emptyCells, cells)

    def solveBacktrack(self, idx, emptyCells, cells):
        if idx >= len(emptyCells):
            return True
        row = emptyCells[idx][0]
        col = emptyCells[idx][1]
        if cells[row][col].val:
            return self.solveBacktrack(idx + 1, emptyCells, cells)
        deep = copy.deepcopy(cells)
        for k in range(1, 10):
            if not cells[row][col].notPossible[k]:
                if self.setCell(row, col, k, cells):
                    if self.solveBacktrack(idx + 1, emptyCells, cells):
                        return True
                cells = deep
        return False


class cell:
    def __init__(self):
        self.val = 0
        self.numPossibilities = 9
        self.notPossible = [0] * 10


s = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
     ["7", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", "2", ".", "1", ".", "9", ".", ".", "."],
     [".", ".", "7", ".", ".", ".", "2", "4", "."],
     [".", "6", "4", ".", "1", ".", "5", "9", "."],
     [".", "9", "8", ".", ".", ".", "3", ".", "."],
     [".", ".", ".", "8", ".", "3", ".", "2", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "6"],
     [".", ".", ".", "2", "7", "5", "9", ".", "."]]
Solution().solveSudoku(s)
print(s)
