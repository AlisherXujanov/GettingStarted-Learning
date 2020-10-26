
def game(secret_num, guess_times):
    times = 0
    game_over = False # remove this
    while guess_times > times and not game_over: # try using while True:
        # how to get out???
        # one method: return False

        guess = int(input("Enter a number please: "))
        times += 1
        att = "attempts"
        if times == 1:
            att = "attempt"
        if guess > secret_num:
            if guess == secret_num + 1:
                print("Too close, a little below than that...")
                print(f"You have {guess_times - times} {att} left")
            else:
                print("Too high...")
                print(f"You have {guess_times - times} {att} left")
        elif guess < secret_num:
            if guess == secret_num - 1:
                print("Too close, a little higher than that...")
                print(f"You have {guess_times - times} {att} left")
            else:
                print("Too below...")
                print(f"You have {guess_times - times} {att} left")
        else:
            return True
            att = "attempts"
            if times == 1:
                att = "attempt"
            print("You got it")
            print(f"It took you {times} {att} in total...")
            game_over = True
    # ifyou reach here, it means you ran out of turns
    return False
