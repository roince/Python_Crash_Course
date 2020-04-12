import random


class Dice:
    dice_roll = (random.randint(1, 6))
    
    def roll(self):
        self.dice_roll = dice_roll = (random.randint(1, 6))


dice1 = Dice()
print(dice)
