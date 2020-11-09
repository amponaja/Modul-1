import random

word_list_benda = ["susu", "motor", "rumah", "pulpen", "sepatu", "angkot", "lemari"]
clue = ["minuman bayi", "kendaraan roda dua", "tempat tinggal", "alat menulis", "alas kaki", "kendaraan umum", "tempat penyimpanan"]

def get_word():
    word = random.choice(word_list_benda)
    return word.lower()

def play(word):
    word_completion = "_" * len(word)
    tries = 6
    print("****** HANGMAN ******")
    print("\n")
    print(len(word), "kata", clue[word_list_benda.index(word)])    
    print(hangman(tries))
    print(word_completion)
    print("\n")
    while word_completion != word and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha(): 
            if guess not in word:
                print(guess, "is not in the word.")
                print(len(word), "kata", clue[word_list_benda.index(word)])                          
                tries -= 1
                print("you have", tries, "tries remaining")               
            else:
                print("Good job,", guess, "is in the word!")
                print(len(word), "kata", clue[word_list_benda.index(word)]) 
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess 
                word_completion = "".join(word_as_list)
        elif len(guess) == len(word) and guess.isalpha():           
            if guess != word:
                print(guess, "is not the word.")
                print(len(word), "kata", clue[word_list_benda.index(word)]) 
                tries -= 1
                print("you have", tries, "tries remaining")               
            else:           
                word_completion = word
        else:
            print("Not a valid guess.")
            print(len(word), "kata", clue[word_list_benda.index(word)]) 
            tries -= 1
            print("you have", tries, "Tries remaining")           
        print(hangman(tries))
        print(word_completion)
        print("\n")
    if word_completion == word or "_" not in word_completion:
        print("You win! the word is " + word)
    elif tries == 0:
        print("You Lose! the word is " + word + ". Maybe next time!")


def hangman(tries):
    stages = [  
                """
--------
|      |
|      O
|     \\|/
|      |
|     / \\
-
                """,
                
                """
--------
|      |
|      O
|     \\|/
|      |
|     / 
-
                """,
                
                """
--------
|      |
|      O
|     \\|/
|      |
|      
-
                """,
                
                """
--------
|      |
|      O
|     \\|
|      |
|     
-
                """,
                
                """
--------
|      |
|      O
|      |
|      |
|     
-
                """,
                
                """
--------
|      |
|      O
|    
|      
|     
-
                """,
                
                """
--------
|      |
|      
|    
|      
|     
-
                """
    ]
    return stages[tries]


def main():
    get_word()
    play(get_word())
    while input("Play Again? (Y/N) ").upper() == "Y":
        get_word()
        play(get_word())


main()

