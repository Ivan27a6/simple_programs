from random import randint

class Object:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine

class GameField:
    "Генерация игрового поля"
    
    # Инициализация поля
    def __init__(self, x=30, y=16, mines=100):
        self._m = x
        self._n = y
        self._mines = mines
        self.field = [[Object() for y in range(self._m)]
                                    for x in range(self._n)]
        self._init()
        self.show()
    
    # Вставка и подсчет окружающих мин
    def _init(self):
        mines = 0
        if self._mines < self._m * self._n: # если мин меньше возможного
            while mines < self._mines:
                x = randint(0, self._n - 1)
                y = randint(0, self._m - 1)
                if self.field[x][y].mine:
                    continue
                self.field[x][y].mine = True
                mines += 1
        
            index = ((-1, -1), (-1, 0), (0, -1), (-1, 0),
                            (0, 0), (1, 0), (0, 1), (1, 1))
            for x in range(self._n):
                for y in range(self._m):
                    if not self.field[x][y].mine:
                        mines = sum((self.field[x+i][y+j].mine
                                            for i, j in index
                                            if 0 <= x + i < self._n
                                            and 0 <= y + j < self._m))
                        self.field[x][y].around_mines = mines
        else:
            for x in range(self._n):
                for y in range(self._m):
                    self.field[x][y].mine = True
    
    # отображение поля
    def show(self):
        for row in self.field:
            print(*map(lambda obj: obj.around_mines
                       if not obj.mine else '*', row))
            
# game_proffesional = GameField()
# print()
# game_advansed = GameField(16, 16, 40)
# print()
# game_beginner = GameField(9, 9, 10)
# print()
game = GameField(2, 2, 5)