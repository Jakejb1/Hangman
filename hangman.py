import random
attempts = 10

with open("words.txt", 'r') as file: 
    lines = file.readlines() 
    random_line = random.choice(lines)
    letterReplace = random_line 
    hidden_word = ['_']*(len(random_line) - 1)
    print(' '.join(hidden_word))
    while attempts > 0:
        letterGuess = input("Guess a single letter.")
        found = False
        for i, letter in enumerate(random_line):
            if letter != "_" and letterGuess == letter:
                hidden_word[i] = letter
                found = True
                print(' '.join(hidden_word))  
        if not found:
            attempts -= 1
            print("You have", attempts, "attempts left.")           
if attempts == 0:
    print("You failed!")
    print(random_line, "was the word.")
