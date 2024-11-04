class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = " "  # Символ клетки ('X', 'O' или пробел)
        self.occupied = False  # Статус занятости клетки

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]  # Создаем 9 клеток для доски

    def display_board(self):
        """Отображает игровую доску."""
        print("-------------")
        for i in range(0, 9, 3):
            print(f"| {self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol} |")
        print("-------------")

    def change_cell(self, cell_number, symbol):
        """Изменяет символ клетки, если она не занята."""
        cell = self.cells[cell_number - 1]
        if cell.occupied:
            return False
        cell.symbol = symbol
        cell.occupied = True
        return True

    def check_game_over(self):
        """Проверяет, завершена ли игра (выигрыш или ничья)."""
        # Проверка строк, столбцов и диагоналей
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикальные линии
            (0, 4, 8), (2, 4, 6)  # диагонали
        ]
        for pos in win_positions:
            if self.cells[pos[0]].symbol != " " and \
               self.cells[pos[0]].symbol == self.cells[pos[1]].symbol == \
               self.cells[pos[2]].symbol:
                return True
        return False

    def reset_board(self):
        """Сбрасывает игровую доску для новой игры."""
        for cell in self.cells:
            cell.symbol = " "
            cell.occupied = False

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0  # Количество побед игрока

    def make_move(self):
        """Запрашивает ход игрока и проверяет корректность ввода."""
        while True:
            try:
                move = int(input(f"{self.name}, введите номер клетки для вашего хода (1-9): "))
                if move < 1 or move > 9:
                    raise ValueError
                return move
            except ValueError:
                print("Неправильный ввод. Пожалуйста, введите число от 1 до 9.")

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = Board()

    def launch_move(self, player):
        """Выполняет ход текущего игрока."""
        while True:
            self.board.display_board()
            cell_number = player.make_move()
            if self.board.change_cell(cell_number, player.symbol):
                if self.board.check_game_over():
                    return True
                return False
            print("Клетка занята. Сделайте другой ход.")

    def play_one_game(self):
        """Проводит одну игру до победы одного из игроков или ничьи."""
        print("Игра началась!")
        while True:
            for player in self.players:
                if self.launch_move(player):
                    self.board.display_board()
                    print(f"Поздравляем, {player.name}! Вы выиграли!")
                    player.wins += 1
                    return
                if all(cell.occupied for cell in self.board.cells):
                    self.board.display_board()
                    print("Ничья!")
                    return

    def start_games(self):
        """Запускает серию игр с возможностью перезапуска."""
        print("Добро пожаловать в игру Крестики-Нолики!")
        while True:
            self.board.reset_board()  # Сбрасываем доску для новой игры
            self.play_one_game()
            print(f"Счет: {self.players[0].name} - {self.players[0].wins}, {self.players[1].name} - {self.players[1].wins}")
            again = input("Хотите продолжить игру? (да/нет): ")
            if again.lower() != 'да':
                print("Спасибо за игру!")
                break

# Создаем двух игроков
player1 = Player("Игрок 1", 'X')
player2 = Player("Игрок 2", 'O')

# Запускаем игру
game = Game(player1, player2)
game.start_games()
