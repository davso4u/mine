class multi_player_game:
    chance = 3
    dice_roll = ""
    desired_dice = 6
    out_of_dice = False

    def roll_dice(self):
        while self.dice_roll != self.desired_dice and not self.out_of_dice:
            if self.chance > 0:
                self.dice_roll = int(input('player1 rolldice: '))
                # self.dice_roll = int(self.dice_roll)
                self.chance -= 1

            else:
                self.out_of_dice = True

            print(f'You have  {self.chance} chance left\ntry again\n')

        if self.out_of_dice:
            print('out of dice, You lose')
        # else:
        #     self.dice_roll = self.desired_dice
        #     print('You Win')
        else:
            print('You Win')

    def checkchance(self):
        if self.chance <= 0:
            print('No more chance')
        # elif self.dice_roll == self.desired_dice:
        #     print('good game won')
        else:
            print('good game won')
        # else:
        #     print(str(self.chance) + ' chances left')

player1 = multi_player_game()
player2 = multi_player_game()
#
player1.roll_dice()
player1.checkchance()
player2.roll_dice()
player2.checkchance()
