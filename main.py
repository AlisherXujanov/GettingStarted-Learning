from random_game import game
import random

if __name__ == "__main__":
    answer = True
    while answer:
        try:
            while answer:
                secret_number = random.randint(0,100)
                game(secret_number)
                user_inp = input("Would you like to try again?? Yes/No: ").upper()
                if user_inp == "YES":
                    continue
                else:
                    print("Thank you for playing...")
                    answer = False
        except:
            print("Invalid input...")
            continue