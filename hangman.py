import random
lives = 3
word = ["hamburger", "chicken", "watermelon", "car", "hangman", "computer"]
def guess():
    user = input("enter a letter to guess: ")
    for i, letter in enumerate(random_word):
        if user == letter and user != "_":
            hidden[i] = letter
        elif user not in random_word:
            return False

random_word = word[random.randint(0, 5)]
hidden = ["_"] * len(random_word)
print(" ".join(hidden))
while lives >= 0:
    print(f"Lives: {lives}")
    if lives == 0:
        print("you ran out of lives")
        print(f"the word was: {random_word}")
        quit()
    x = guess()
    if x == False:
        lives -= 1
    print(" ".join(hidden))
    if "_" not in hidden:
        print("you won")
        quit()
