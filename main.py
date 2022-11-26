import random

class Random:

    def __init__(self, num_to_guess: int = 0, num: int = 0):
            self.num = num
            self.num_to_guess = num_to_guess
            self.min = 1
            self.max = 10

        # Play game while true
            while True :
                self.num_to_guess = self.get_rand(self.min, self.max)
                self.num = self.get_proposal(self.min, self.max)

                if self.num_to_guess == self.num:
                    return print("You Win ! It was -> ", self.num_to_guess), self.try_again()
                else:
                    print("You Loose... The Number to Guess was -> ", self.num_to_guess)
                    self.try_again()

    # get arandom number between min/max
    def get_rand(self, min: int, max: int) -> int:
        return random.randint(min, max)

    def get_proposal(self, min, max) -> int:
        # Ask to guess a number while true
        while True :
            num = input(f" Guess a number betwen {min} and {max} : ")
            try:
                num = int(num)
                # if answer is not correct, ask again
                if num > max or num < min:
                    print(f"The Number to Guess is only between {min} and {max} ")
                    return self.get_proposal(self.min, self.max)
                # if num value is correct, return value
                return num
            except ValueError:
                print("ValueError: only numbers are required")
    
    def try_again(self) -> str:
        answer = input("Try Again ? ( Y / N ) => ").lower()
        while True :
            try:
                if answer == 'y':
                    # if 'Y' or 'y', go to init while True
                    break
                elif answer == 'n':
                    # si 'N' or 'n' exit()
                    exit("Ok Bye")
                else:
                    return self.try_again()
            except TypeError:
                print("TypeError on try_again Method")


Random()