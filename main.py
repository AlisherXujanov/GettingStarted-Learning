def game(secret_num, guess_times):
    times = 0
    game_over = False
    while guess_times > times and not game_over:
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
            att = "attempts"
            if times == 1:
                att = "attempt"
            print("You got it")
            print(f"It took you {times} {att} in total...")
            game_over = True

game(29, 10)
