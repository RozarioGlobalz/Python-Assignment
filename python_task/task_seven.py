import random


def play_game():
    
    guess = int(input("Guess a number from 1 - 1000  "))
    secret_number = random.randrange(1, 1000)
    
   
    while True:
        
        guess_number = int(input("guess a number"))
        
        
        if guess_number < secret_number:
            
            print("Too low jor!..goooo higher")
            
    
        if guess_number > secret_number:
          
            print("Too high bro!!! go lower")
            
        
        if guess_number == secret_number:
         
            print("correct number")
            break

print(play_game())
















