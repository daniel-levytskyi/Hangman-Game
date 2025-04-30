import random
lives = 3
word = "hamburger"
def guess():
    user = input("enter a letter to guess: ")
    for i, letter in enumerate(word):
        if user == letter and user != "_":
            hidden[i] = letter
        elif user not in word:
            return False

hidden = ["_"] * len(word)
print(" ".join(hidden))
while lives >= 0:
    print(f"{lives}")
    if lives == 0:
        print("you ran out of lives")
        quit()
    x = guess()
    if x == False:
        lives -= 1
    print(" ".join(hidden))
    if "_" not in hidden:
        print("you won")
        quit()
