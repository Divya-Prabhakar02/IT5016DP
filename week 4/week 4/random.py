import random
def usernumber_guess(computer_num):
    prompt = "enter your guess(1-99):"
    while computer_num < 100:
        print("TOO HIGH")
        count = count+1
def main():
    usernumber_guess(random.randrange(1,100)) 
main()       
