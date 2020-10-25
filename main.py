times = 0
guess = int()
secret_num = 29
guess_times = 3
out_of_guesses = False

while guess != secret_num and not out_of_guesses and guess_times > 0:
    times += 1
    guess_times -= 1
    att = "attempts"
    if att == 1:
        att = "attempts"
    guess = int(input("Guess a number: "))
    if guess > secret_num:
        if guess == secret_num + 1:
            print("Too close...A little down...")
            print(f"You have {guess_times} {att} left!")
        else:
            print("Too high...")
            print(f"You have {guess_times} {att} left!")
    elif guess < secret_num:
        if guess == secret_num - 1:
            print("Too close...A little higher...")
            print(f"You have {guess_times} {att} left!")
        else:
            print("Too below...")
            print(f"You have {guess_times} {att} left!")
    else:
        print("CONGRATULATIONS...")
    if guess_times == 0:
        out_of_guesses = True

if out_of_guesses:
    print("You lose... Try again next time")
else:
    print(f"It took you {times} {att} in total...")
