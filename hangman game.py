
import random

def hangman():
    words = ['python', 'programming', 'computer', 'keyboard', 'developer']
    secret_word = random.choice(words)
    guessed_letters = []
    tries = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")
    
    while tries > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print(f"\nWord: {display_word}")
        print(f"Tries left: {tries}")
        
        if '_' not in display_word:
            print("Congratulations! You won!")
            break
            
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")
    
    if tries == 0:
        print(f"\nGame over! The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
