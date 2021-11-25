import random
import collections


# Farkle/game class


class Farkle:
    turnCount = 0
    diceCount = 0
    numberOfRolledDice = 0

    def dice(self, number_of_rolled_dice):
        return [random.randint(1, 6) for _ in range(number_of_rolled_dice)]

    def roll(self):
        pass

    def roll_check(self):
        rolling = True
        while rolling:
            try:
                dice_remaining = int(input("How many dice do you wish to roll?"))
            except ValueError:
                print("This is an unaccepted response, enter a valid value")
                continue
            else:
                if dice_remaining >= 1:
                    print("Good luck on your roll!!!")
                else:
                    rolling = False

    def save(self):
        pass

    def load(self):
        pass

    def turn(self):
        pass
        '''
        Dice rolled first
        Hand is created and displayed
        Check for score that's possible, if none then skip to end
        ask for user input on how many dice they wish to re-roll
        verify that you can earn score with the dice that you loose on re-roll
        loop through this until player calls quits or the player has no points earned in a turn 
        if score is earned and not "farkled" then append score of player with Character.gain_score
        increase turn counter
        '''
        while True:
            hand = Farkle.dice(6)


# Player class


class Character:
    chrCount = 0
    score = 0

    def __init__(self, name):
        self.current_Roll = None
        self.total_Roll = None
        self.name = name
        Character.chrCount += 1

    def gain_score(self, increased_score):
        self.score = int(self.score) + int(increased_score)

    def display_score(self):
        print(str(self.name) + ":" + str(self.score))


# Main game loop
# Menu


def score_check(my_roll, sides=6):
    dice_list = [0] * sides
    die_score = 0
    gained_score = 0
    counts = collections.Counter(my_roll)
    single_values = {1: 100, 5: 50}
    for i, count in enumerate(dice_list):
        dice = i + 1
    for die, count in counts.items():
        die_score += single_values.get(die, 0) * count
        if count == 4:
            die_score += die * 2000 if die == 1 else die * 200
            count -= 4
        elif count == 3:
            die_score += die * 1000 if die == 1 else die * 100
            count -= 3

    gained_score += die_score
    return gained_score


def scoring_values():
    pass


fallen = Character("fallen")
highest_score = 0

while highest_score < 10000:
    game = Farkle()
    rolled_dice = game.dice(6)
    print(rolled_dice)
    print(score_check(rolled_dice))
    fallen.gain_score(score_check(rolled_dice))
    if fallen.score <= 499:
        fallen.score = 0
    #fallen = Character("fallen")

    print(fallen.display_score())
    highest_score = fallen.score

