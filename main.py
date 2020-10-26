from random_game import game
import random

if __name__ == "__main__":
    secret_number = random.randint(0,100)
    result = game(secret_number)