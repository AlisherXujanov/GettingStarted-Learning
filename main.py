from random_game import game
import random

if __name__ == "__main__":
    secret_number = random.randint(0,100)
    result = game(secret_number, 10)
    if result is False:# delete
        print('You lose!')# delete
    elif result is True:# delete
        print('You win!')# delete
