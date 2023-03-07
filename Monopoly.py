import random

class Player:
    def __init__(self, board, loc = 0):
        self.board = board
        self.loc = loc
        self.doubles = 0
        self.jail = False
        self.jail_rolls = 0

    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dbl = dice1 == dice2
        if dbl and self.doubles == 2:
            self.loc = 10
            self.doubles = 0
            self.jail = True
            self.print_loc(dice1, dice2)
        else:
            self.loc = (self.loc + dice1 + dice2) % 40
            self.print_loc(dice1, dice2)
            if self.check_special():
                self.special()
            if dbl:
                self.doubles += 1
                self.roll()

    def roll_jail(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.jail_rolls += 1
        if dice1 == dice2 or self.jail_rolls == 3:
            self.loc = (self.loc + dice1 + dice2) % 40
            self.print_loc(dice1, dice2)
            if self.check_special():
                self.special()
            self.jail_rolls = 0
            self.jail = False
        else:
            self.jail_rolls += 1
            self.print_loc(dice1, dice2)

    def check_special(self):
        return self.loc in self.board.chance or self.loc in self.board.community_chest
    
    def special(self):
        if self.loc in self.board.chance:
            actions = [39, 0, 24, 11, "railroad", "railroad", "utility", "back", "jail", 5]
            r = random.randint(1, 16)
            if r < 10:
                if actions[r] == "railroad":
                    pass
                elif actions[r] == "utility":
                    pass
                elif actions[r] == "back":
                    pass
                elif actions[r] == "jail":
                    pass
                else:
                    self.loc = actions[r]
                    self.print_loc()
        if self.loc in self.board.community_chest:
            actions = [0, "jail"]
            r = random.randint(1, 16)
            if r < 3:
                if r == 1:
                    pass
                else:
                    self.loc = actions[r]
                    self.print_loc()
        else:
            self.jail = True
            self.loc = 10

    def nearest_railroad(self):
        pass
    
    def nearest_utility(self):
        pass
    
    def back(self):
        pass
    
    def go_to_jail(self):
        pass

    def print_loc(self, dice1 = None, dice2 = None):
        if dice1 and dice2:
            print("{}+{}={}, {}".format(dice1, dice2, dice1 + dice2, self.board.locations[self.loc])) 
        else:
            print(self.board.locations[self.loc])

    def sim_turn(self):
        if self.jail:
            self.roll_jail()
        else:
            self.roll()

class Location:
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc

class Board:
    def __init__(self):
        self.board = []
        self.locations = [
        "Go",
        "Mediterranean Avenue",
        "Community Chest",
        "Baltic Avenue",
        "Income Tax",
        "Reading Railroad",
        "Oriental Avenue",
        "Chance",
        "Vermont Avenue",
        "Connecticut Avenue",
        "Jail",
        "St. Charles Place",
        "Electric Company",
        "States Avenue",
        "Virginia Avenue",
        "Pennsylvania Railroad",
        "St. James Place",
        "Community Chest",
        "Tennessee Avenue",
        "New York Avenue",
        "Free Parking",
        "Kentucky Avenue",
        "Chance",
        "Indiana Avenue",
        "Illinois Avenue",
        "B. & O. Railroad",
        "Atlantic Avenue",
        "Ventnor Avenue",
        "Water Works",
        "Marvin Gardens",
        "Go To Jail",
        "Pacific Avenue",
        "North Carolina Avenue",
        "Community Chest",
        "Pennsylvania Avenue",
        "Short Line Railroad",
        "Chance",
        "Park Place",
        "Luxury Tax",
        "Boardwalk"]
        for i, location in enumerate(self.locations):
            self.board.append(Location(location, i))
        self.chance = [7, 22, 36]
        self.community_chest = [2, 17, 33]

if __name__ == "__main__":
    board = Board()
    player1 = Player(board)
    for i in range(5):
        player1.sim_turn()