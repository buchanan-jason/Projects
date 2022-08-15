correct_answer = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == correct_answer:
        print("You won")
        break
else:
    print("Out of guesses. You lost.")

