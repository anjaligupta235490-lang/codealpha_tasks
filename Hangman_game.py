import random
words = ["python", "hangman", "coding", "programming", "developer", "algorithm", "function"]
word = random.choice(words)
guessed = ["_"] * len(word)
guessed_letters= []
attempts = 6
print("=== welcome to Hangman Game ===")
print("Guess the word:")
print(" ".join(guessed))
while attempts > 0 and "_"in guessed:
    guess = input("\nEnter a letter:").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("please enter only alphabet letter")
        continue

    if guess in guessed_letters:
        print("\nYou already guessed that letter!")
        continue

    guessed_letters.append(guess)
    if guess  in word:
        print("Correct guess !")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:",attempts)
    print(" ".join(guessed))
    print("Guessed letters:", ", ".join(guessed_letters))


if "_" not in guessed:
    print("\nCongretulations! You win!" )
    print("The word was:", word)
else:
    print("\nBetter luck next time")
    print("The word was:", word)

          

   


