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
        if dbl:
            self.doubles += 1
        else:
            self.doubles = 0
        if self.doubles >= 3:
            self.go_to_jail()
            self.print_loc()
        else:
            self.loc = (self.loc + dice1 + dice2) % 40
            self.print_loc(dice1, dice2)
            if self.check_special():
                self.special()
            if dbl:
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
        return self.loc in self.board.chance or self.loc in self.board.community_chest or self.loc == 30
    
    def special(self):
        if self.loc in self.board.chance:
            chance_actions = [39, 0, 24, 11, "railroad", "railroad", "utility", "back", "jail", 5, None, None, None, None, None, None]
            random.shuffle(chance_actions)
            card = chance_actions.pop()
            if card:
                if card == "railroad":
                    self.nearest_railroad()
                elif card == "utility":
                    self.nearest_utility()
                elif card == "back":
                    self.back_three_spaces()
                elif card == "jail":
                    self.go_to_jail()
                else:
                    self.loc = card
                self.print_loc()
        elif self.loc in self.board.community_chest:
            community_chest_actions = [0, "jail", None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            random.shuffle(community_chest_actions)
            card = community_chest_actions.pop()
            if card:
                if card == "jail":
                    self.go_to_jail()
                else:
                    self.loc = card
                self.print_loc()
        else:
            self.go_to_jail()
            self.print_loc()

    def nearest_railroad(self):
        railroads = [5, 15, 25, 35]
        if self.loc > 35:
            self.loc = 5
        else:
            for i, loc in enumerate(railroads):
                if self.loc <= loc <= self.loc + 10:
                    self.loc = railroads[i]
                    break

    
    def nearest_utility(self):
        if 12 < self.loc <= 28:
            self.loc = 28
        else:
            self.loc = 12
    
    def back_three_spaces(self):
        self.loc = self.loc - 3 % 40
    
    def go_to_jail(self):
        self.loc = 10
        self.jail = True
        self.doubles = 0
        self.jail_rolls = 0

    def print_loc(self, dice1 = None, dice2 = None):
        if dice1 and dice2:
            print("{}+{}={}, {} {}".format(dice1, dice2, dice1 + dice2, self.board.locations[self.loc], self.loc)) 
        else:
            print(self.board.locations[self.loc], self.loc)

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
    turns = int(input("Enter number of turns: "))
    for i in range(turns):
        print("Turn " + str(i+1))
        player1.sim_turn()