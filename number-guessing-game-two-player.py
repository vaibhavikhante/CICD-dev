max_num = 1000

continue_game = "Y"

while continue_game == "Y":
    while True:
        secret_num = input("Player One, give me a number: ")
        if secret_num.isdigit():
            secret_num = int(secret_num)
            if secret_num > max_num:
                print ("Sorry, the number needs to be less than", max_num)
            else:
                break
        else:
            print ("Sorry, I really need a number")

    for i in range(1):
        print ("Don't look, Game Master!")

    guess = -1

    while guess != secret_num:
        while True:
            guess = input("Game Master, what's your guess? ")
            if guess.isdigit():
                guess = int(guess)
                break
            else:
                print ("Sorry, I really need a number")

        if guess == secret_num:
            print ("You got it!")
        elif guess > secret_num:
            print ("Hmm, that's big...")
        else:
            print ("Nope, that's small.")

    continue_game = input("Want another game [Y/N]?")