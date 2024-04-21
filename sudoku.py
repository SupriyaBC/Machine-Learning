import tkinter as tk
from tkinter import messagebox

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Sudoku Game')
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.solution = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        self.selected = None
        self.cells = {}
        self.draw_board()

    def draw_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    cell = tk.Label(self.root, text=str(self.board[i][j]), font=('Arial', 16), width=3, relief='ridge')
                    cell.grid(row=i, column=j)
                else:
                    cell = tk.Entry(self.root, width=3, font=('Arial', 16))
                    cell.grid(row=i, column=j)
                    cell.bind('<FocusIn>', lambda e, i=i, j=j: self.select_cell(i, j))
                    self.cells[(i, j)] = cell

    def select_cell(self, i, j):
        if self.selected:
            self.cells[self.selected].config(bg='white')
        self.selected = (i, j)
        self.cells[self.selected].config(bg='lightblue')

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.solution[i][j]:
                    return False
        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_valid(row, col, i):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0

        return False

    def is_valid(self, row, col, num):
        # Check row
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False

        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def validate(self):
        if self.check_solution():
            messagebox.showinfo('Sudoku', 'Congratulations! Puzzle solved.')
        else:
            messagebox.showerror('Sudoku', 'Try again!')

    def clear(self):
        for cell in self.cells.values():
            cell.delete(0, tk.END)

    def play(self):
        validate_button = tk.Button(self.root, text='Validate', command=self.validate)
        validate_button.grid(row=9, column=0, columnspan=4)

        solve_button = tk.Button(self.root, text='Solve', command=self.solve)
        solve_button.grid(row=9, column=4, columnspan=4)

        clear_button = tk.Button(self.root, text='Clear', command=self.clear)
        clear_button.grid(row=9, column=8, columnspan=4)

if __name__ == '__main__':
    root = tk.Tk()
    game = SudokuGame(root)
    game.play()
    root.mainloop()
