import configparser
import random
from casino_logic import calculate_win_loss

class CasinoGame:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self.starting_money = int(config['DEFAULT']['MY_MONEY'])
        self.current_money = self.starting_money

    def play(self):
        while True:
            bet = int(input("Place your bet: "))
            winning_slot = random.randint(1, 10)
            result = calculate_win_loss(bet, winning_slot)
            if result > 0:
                print(f"You win! Your winnings: ${result}")
            else:
                print("You lose!")
            self.current_money += result
            print(f"Current money: ${self.current_money}")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break
        print("Game over. Final balance:", self.current_money)