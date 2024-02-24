from game_logic import choose_word, take_guess, display_word

def play_game():
    print("=== Guess the Word Game ===")
    selected_word = choose_word()
    guessed_letters = set()
    attempts_left = 6

    while attempts_left > 0:
        guess = take_guess()

        if guess in guessed_letters:
            print("You already guessed this letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in selected_word:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")
        else:
            print("Correct guess!")

        current_display = display_word(selected_word, guessed_letters)
        print("Current state of your guess:", current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word correctly.")
            break

    if attempts_left == 0:
        print(f"Sorry, you ran out of attempts. The correct word was: {selected_word}")

if __name__ == "__main__":
    play_game()
