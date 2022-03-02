import randomwords
import random
import string
visuals = {1:'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 2:'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 3:'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',4: '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',5:  '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 6:'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 7:'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''}
def get_random_word(choice):
    if choice == "1":
        word = random.choice(randomwords.words)
        while len(word)<10 and "-" not in word and " " not in word:
            word = random.choice(randomwords.words)
        
    elif choice == "0":
        word = random.choice(randomwords.words)
        while "-" in word or " " in word:
            word = random.choice(randomwords.words)
    else:
        print("Exit.")
        exit()
    return word
def hangman():
    choice = input("Enter 0 for Easy or 1 for Hard:")
    word = get_random_word(choice).upper()
    word_letters = list(word)
    alpha = list(string.ascii_uppercase) + [" ", "-"]
    used = []
    wrongguesses = 0
    while len(word_letters) > 0 and wrongguesses < 7:
        currentword = [x if x in used else "_" for x in word]
        print(visuals[7-wrongguesses])
        print(" ".join(currentword))
        guess = input("Guess a letter ").upper()
        if guess in alpha and guess not in word_letters:
            print("Wrong!")
            wrongguesses +=1
            used.append(guess)

        elif guess in alpha and guess not in used:
            used.append(guess)
            while guess in word_letters:
                word_letters.remove(guess)
        elif guess in used:
            print("You've already guessed that letter.")
        else:
            print("Invalid character")

        if len(word_letters) == 0:
            print("Congratulations! You won, the word was " + word)
            exit()
        if wrongguesses == 7:
            print("You lost, the word was " + word)
            exit()
        print("You have used these letters: ", " , ".join(used))
        print("You have " + str(7-wrongguesses) + " wrong guesses left.")
hangman()