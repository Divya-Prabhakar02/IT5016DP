import random
def usernumber_guess(computer_num):
    prompt = "enter your guess(1-99)"
    num_guesses = 0
    number = 0
    while number != computer_num:
        number = int(input(prompt))
        num_guesses += 1
        if number <computer_num:
            print("TOO LOW")
        elif number> computer_num:
            print("TOO HIGH")
        else:
            print(f"correct! numer of guess; {num_guesses}")
def main():
        usernumber_guess(random.randrange(1,100)) 
main()       
