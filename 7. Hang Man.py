#from replit import clear
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
guessed_letters=""
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #clear()
   
    if guess in guessed_letters:
        print(f"You have already guessed the letter: {guess}")
        print(display)
    else:
   
        for position in range(word_length):
            letter = chosen_word[position]
           
            if letter == guess:
                display[position] = letter
        
        if guess not in chosen_word:
            print(f"{guess} is not a letter in the chosen word. You lose a life!")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
    
        print(f"{' '.join(display)}")
        guessed_letters += guess
        
        if "_" not in display:
            end_of_game = True
            print("You win.")
    
    print(hangman_art.stages[lives])

print(f"The word was: {chosen_word}")