import random

target = random.randint(1, 10)
attempts = 3

print("Guess the number (1-10)")
while attempts > 0:
    guess = int(input("Your guess: "))
    if guess == target:
        print("Correct! You win!")
        break
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left.")
else:
    print(f"Game over! Number was {target}")