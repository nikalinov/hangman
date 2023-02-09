import random


tries, wins, losses = 8, 0, 0


def main():
    global tries, wins, losses
    words = ["python", "java", "swift", "javascript"]
    guessed = random.choice(words)

    hyphened = ["-"] * len(guessed)
    used_letters = [] # List of already guessed letters
    i = 0  # Number of tries used
    while i < tries:

        print(f"{''.join(hyphened)}\nInput a letter: ", end="")
        guessed_letter = input()

        # Letter validity check
        if len(guessed_letter) != 1:
            print("Please, input a single letter.")
            continue
        elif guessed_letter < "a" or guessed_letter > "z":
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        successful_guess = False
        # If the guessed letter appears in the word,
        # change corresponding hyphens
        for j, letter in enumerate(guessed):
            if guessed_letter == letter:
                hyphened[j] = letter
                successful_guess = True

        # If the guess is not successful
        if not successful_guess:
            i += 1
            print(f"That letter doesn't appear in the word. ", end="")

        # If guessed letter has been entered before, print the message,
        # else add to the list
        if guessed_letter in used_letters:
            print("You've already guessed this letter.")
        else:
            used_letters.append(guessed_letter)

        print(f" # {tries - i} attemts\n")

        # If the word is guessed successfully, exit
        if "".join(hyphened) == guessed:
            print(f"You guessed the word {guessed}!\nYou survived!")
            wins += 1
            tries = 8
            break
    else:
        print("You lost!")
        losses += 1
        tries = 8


choice = ""
while choice != "exit":
    print(f"H A N G M A N  # {tries} attempts\n")
    print("""Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:""")
    choice = input()
    if choice == "play":
        main()
    elif choice == "results":
        print(f"You won: {wins} times\nYou lost: {losses} times")


