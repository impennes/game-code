class Game():
    def __init__(self):
        self.game_active = False
        self.menu = Menu()
        self.health = 100

    def health_change(self, ammount):
        self.health += ammount


class Menu():
    def __init__(self):
        pass


class Level():
    pass


class Player():
    pass

