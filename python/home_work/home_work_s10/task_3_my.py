from random import randint
import time
class Board:
    def __init__(self):
        self.data = [['-', '-', '-'],
                     ['-', '-', '-'],
                     ['-', '-', '-']]

    def chage_position(self,y,x,credo):
        if self.data[y][x] == "-":
            self.data[y][x] = credo
            # делаем красивый вывод
            for i in self.data:
                print(*i, sep="\t|\t")
                print('-' * 18)
            print()
        else:
            print("\n\tВы пытаетесь переписать значения противника либо свое!\n")

    def cheak_win(self,emblem):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if   self.data[i][0] == emblem and self.data[i][1] == emblem and self.data[i][2] == emblem:
                    return True
                elif self.data[0][j] == emblem and self.data[1][j] == emblem and self.data[2][j] == emblem:
                    return True
                elif self.data[0][0] == emblem and self.data[1][1] == emblem and self.data[2][2] == emblem:
                    return True
                elif self.data[2][2] == emblem and self.data[1][1] == emblem and self.data[0][2] == emblem:
                    return True


class Random_user:
    def __init__(self,Board,User):
        self.name = 'Terminator'
        self.Board = Board
        self.User = User
        self.credo = 'X' if self.User.credo == '0' else "0"

    def move(self):
        free_data = []
        for i, row in enumerate(self.Board.data):
            for j, value in enumerate(self.Board.data[i]):
                if value == "-":
                    free_data.append((i,j))

        if free_data:
            per = randint(0, len(free_data)-1)
            random_y, random_x = free_data[per][0], free_data[per][1]
            return random_x,random_y

class User:
    def __init__(self,name,Board):
        self.name = name
        self.win = 0
        self.Board = Board
        self.count_to_win = 0
        self.credo = input("Введите сторону, за которую хотите играть 'X' или '0' - ")
    def make_move(self):
        x = int(input("Введите координату х - "))-1
        y = int(input("Введите координату у - "))-1
        self.Board.chage_position(y,x,self.credo)
        if self.Board.cheak_win(self.credo):
            self.count_to_win += 1
            print(f'\t\nИгрок {self.name} одержал победу!. Количество побед {self.count_to_win}')
        if not any('-' in row for row in self.Board.data):
            print("Все клетки заполнены, ничья!")


def main():
    board = Board()
    user = User('Oleg', board)
    random_user = Random_user(board,user)
    current_turn = 'User' if user.credo == 'X' else 'Random_user'
    while True:
        if current_turn == 'User':
            print(f"Ваш ход {user.name}")
            user.make_move()
            if user.Board.cheak_win(user.credo):
                break
            current_turn = 'Random_user'
        else:
            print(f'Сейчас ходит {random_user.name}')
            time.sleep(2)
            x, y = random_user.move()
            board.chage_position(y, x,random_user.credo)
            if board.cheak_win(random_user.credo):
                print(f'{random_user.name} выигрывает!')
                break
            current_turn = 'User'

        if not any('-' in row for row in board.data):
            print("Все клетки заполнены, ничья!")
            break

if __name__ == "__main__":
    main()




