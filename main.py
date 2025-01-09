import random

def zenmode():
    print("You are playing zen mode now!")
    print("""Enter "-1" to Quit""")
    r = random.randint(1,100)
    n = 0

    while n != r:
        n = int(input("Enter your guess: "))
        if n < r:
            print("Guess higher!")
        elif n > r:
            print("Guess lower!")
        elif n == r:
            print(f"You guessed {n} in {attempts} attempts")
            break
        elif n == -1:
            print(f"You Finished Zen mode with {attempts} attempts.")
            break
        attempts += 1

def game(difficulty):
    def guessing(attempt):
        r = random.randint(1,100)
        attempts = 1
        n = 0
        i = 0  # Initialize the counter

        while i < attempt:
            print(r)
            print(f"S:{attempts}, T:{attempt}")
            n = int(input("Enter your guess: "))
            if n < r:
                print("Guess higher!")
            elif n > r:
                print("Guess lower!")
            elif n == r:
                print(f"You guessed {n} in {attempts} attempts")
            attempts += 1
            i += 1
        if attempts-1 == attempt:
            print("You ran out of chances")
            

    attempt = 0
    print(f"Great! You have selected the {difficulty} difficulty level.")
    if difficulty == "Easy":
        attempt = 10
        guessing(attempt)
    elif difficulty == "Medium":
        attempt = 5
        guessing(attempt)
    elif difficulty == "Hard":
        attempt = 3
        guessing(attempt)

    
        
def main():    
    print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
4. Zen Mode
5. Exit\n""")
    
    n = int(input("Enter your choice: "))
    try:
        if n == 1:
            a = "Easy"
            game(a)
        elif n == 2:
            a = "Medium"
            game(a)
        elif n == 3:
            a = "Hard"
            game(a)
        elif n == 4:
            zenmode()
        elif n == 5:
            choice = input("Enter Y to continue and X to exit: ")
            choice = choice.upper()
            if choice == "Y":
                main()
    except Exception:
        print(f"Invalid Choice! {n}")

print("""\nWelcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n""")    
main()

