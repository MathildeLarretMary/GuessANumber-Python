import random

class Random:
    
    def __init__(self, num_to_guess : int = 0, num : int = 0):
        
        self.num = num
        self.num_to_guess = num_to_guess
        self.min = 1
        self.max = 10
        
        if self.num == 0:
            self.num_to_guess = self.get_rand(self.min, self.max)
            self.num = self.get_proposal(self.min, self.max)
        
        if self.num_to_guess == self.num:
            return print("You Win ! It was -> ", self.num_to_guess), self.try_again()
        else :
            print("You Loose... The Number to Guess was -> ", self.num_to_guess)
            self.try_again()
        
    def get_rand(self, min : int, max : int) -> int:
        return random.randint(min, max)
    
    def get_proposal(self, min, max) -> int:
        try :
            return int(input(f" Guess a number betwen {min} and {max} : "))
        except ValueError:
            print("ValueError: only numbers are required")
            Random()
            exit(0)
            
    def try_again(self) -> str: 
        answer = input("Try Again ? ( Y / N ) => ").lower()
        try:        
            if answer == 'y':
                Random()
            elif answer == 'n':
                return
            return self.try_again()
        except TypeError:
            print("TypeError on try_again Method")

        
Random()