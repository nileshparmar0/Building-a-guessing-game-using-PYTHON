#The output will keep processing until you enter the exact input that you set!

secret_word  = "Giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter a guess: ")

print("You win")
