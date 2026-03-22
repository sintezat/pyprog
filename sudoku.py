import tkinter as tk
import random


class Sudoku9x9:
    def __init__(self):
        # Создаем окно
        self.window = tk.Tk()
        self.window.title("Судоку 9x9")

        # Генерируем новую доску
        self.generate_new_board()

        # Создаем игровое поле
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_board()

        # Кнопка для новой игры
        btn = tk.Button(self.window, text="Новая игра",
                        font=('Arial', 12), command=self.new_game)
        btn.grid(row=9, column=0, columnspan=9, pady=10)

        # Запускаем игру
        self.window.mainloop()

    def generate_new_board(self):
        """Генерирует новую случайную доску"""
        # Создаем пустую доску
        self.board = [[0 for _ in range(9)] for _ in range(9)]

        # Заполняем первую строку случайными числами 1-9
        nums = list(range(1, 10))
        random.shuffle(nums)
        self.board[0] = nums.copy()

        # Простое заполнение остальных строк (сдвигом)
        for row in range(1, 9):
            # Сдвигаем предыдущую строку на 3 позиции
            shift = 3
            self.board[row] = self.board[row - 1][shift:] + self.board[row - 1][:shift]

        # Удаляем часть чисел (создаем пустые клетки)
        empty_count = 45  # Оставляем примерно 36 чисел (сложность средняя)
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)

        for i in range(empty_count):
            r, c = positions[i]
            self.board[r][c] = 0

    def create_board(self):
        """Создает графическое поле"""
        for row in range(9):
            for col in range(9):
                value = self.board[row][col]

                # Если клетка не пустая
                if value != 0:
                    label = tk.Label(
                        self.window,
                        text=str(value),
                        font=('Arial', 18, 'bold'),
                        width=3, height=1,
                        relief='solid',
                        borderwidth=1
                    )
                    label.grid(row=row, column=col, padx=1, pady=1)
                    self.cells[row][col] = label

                # Если клетка пустая
                else:
                    entry = tk.Entry(
                        self.window,
                        font=('Arial', 18),
                        width=3,
                        justify='center'
                    )
                    entry.grid(row=row, column=col, padx=1, pady=1)
                    entry.bind('<KeyRelease>',
                               lambda e, r=row, c=col: self.check_number(r, c))
                    self.cells[row][col] = entry

        

    def check_number(self, row, col):
        """Проверяет правильность введенного числа"""
        entry = self.cells[row][col]
        text = entry.get()

        # Проверяем что введено число
        if text and text.isdigit():
            num = int(text)

            # Проверяем число от 1 до 9
            if 1 <= num <= 9:
                # Проверяем можно ли поставить число в эту клетку
                if self.is_valid_move(row, col, num):
                    entry.config(bg='lightgreen')
                    entry.config(state='disabled')
                else:
                    entry.config(bg='lightcoral')
                    # Очищаем поле через секунду
                    self.window.after(1000, lambda: entry.delete(0, 'end'))
                    self.window.after(1000, lambda: entry.config(bg='white'))
            else:
                # Число не в диапазоне 1-9
                entry.delete(0, 'end')
                entry.config(bg='yellow')
                self.window.after(500, lambda: entry.config(bg='white'))

    def is_valid_move(self, row, col, num):
        """Проверяет можно ли поставить число в клетку"""
        # Проверяем строку
        for c in range(9):
            if c != col and self.get_cell_value(row, c) == num:
                return False

        # Проверяем столбец
        for r in range(9):
            if r != row and self.get_cell_value(r, col) == num:
                return False

        # Проверяем квадрат 3x3
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if (r != row or c != col) and self.get_cell_value(r, c) == num:
                    return False

        return True

    def get_cell_value(self, row, col):
        """Получает значение из клетки (число или None)"""
        cell = self.cells[row][col]
        if isinstance(cell, tk.Label):
            return int(cell['text'])
        elif isinstance(cell, tk.Entry):
            text = cell.get()
            return int(text) if text and text.isdigit() else 0
        return 0

    def new_game(self):
        """Начинает новую игру"""
        # Удаляем все клетки
        for row in range(9):
            for col in range(9):
                if self.cells[row][col]:
                    self.cells[row][col].destroy()

        # Генерируем новую доску
        self.generate_new_board()

        # Создаем поле заново
        self.create_board()


# Запускаем игру
if __name__ == "__main__":
    Sudoku9x9()
