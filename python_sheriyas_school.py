import random as rd

random_no = rd.randint(1,10)
tries = 0

while True:
    guess_no = int(input("Guess a no: "))
    if guess_no == random_no:
        tries += 1
        print(f"You have guessed right in {tries} attempt")
        break
    elif guess_no < random_no:
        tries += 1
        print("Go little higher")
    elif guess_no > random_no:
        tries += 1
        print("Go little lower")