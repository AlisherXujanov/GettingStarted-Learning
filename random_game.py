
def game(secret_num):
        # how to get out???
        # one method: return False
        # another method: use "break" and "continue" within the "while" loop
        # Homework: get it working with while true, and no return from the function until game is over and you have printed the score
    times = 0
    while True:
        guess = int(input("Enter a number please: "))
        times += 1

        att = "attempts"
        if times == 1:
            att = "attempt"

        if guess > secret_num:
            if guess == secret_num + 1:
                print("Too close, a little below than that...")
            else:
                print("Too high...")
            continue
        elif guess < secret_num:
            if guess == secret_num - 1:
                print("Too close, a little higher than that...")
            else:
                print("Too below...")
            continue
        else:
            print(f"It took you {times} {att} in total...")
            break
    # ifyou reach here, it means you ran out of turn
game(56)
