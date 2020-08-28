import random


class BSearch:  # Simple Binary Search from 0 - 100

    def __init__(self, guess_num=random.randint(0, 100), num_max=100):  # guess_num will be random if
        self.guess = 1  # number of tries before finding correct number
        self.min = 0
        self.max = num_max
        self.to_guess = guess_num  # Number to Guess
        self.cur_guess = round((self.max + self.min) /
                               2)  # Current Guess number
        print(f"Your current number is {self.to_guess}")

    def new_guess(self):
        self.cur_guess = round((self.max + self.min) /
                               2)  # Current Guess number
        return

    def guess_number(self):
        if self.max < self.to_guess or self.max <= 0 or self.min > self.to_guess:
            if self.max < self.to_guess:
                print(
                    f"The max number {self.max} is less than the number to guess {self.to_guess}.")
            elif self.max <= 0:
                print(f"Max number cannot be less than or equal to 0.")
            elif self.min > self.to_guess:
                print(f"The number you picked is less than 0.")
            quit()
        while self.to_guess != self.cur_guess:
            if self.cur_guess < self.to_guess:
                self.min = self.cur_guess
                print(f"{self.cur_guess} < {self.to_guess}")

            elif self.cur_guess > self.to_guess:
                self.max = self.cur_guess
                print(f"{self.cur_guess} > {self.to_guess}")

            self.guess += 1
            self.new_guess()
            print(
                f"Minimum Number is {self.min} and Maximum Number is {self.max}. Changing Guess to {self.cur_guess}.")
        else:
            print(
                f"\nThe Computer have guessed {self.cur_guess} as your number.")
            print(
                f"Number of Tries before finding the number is {self.guess} \n")


for x in range(101):  # Loop code x101
    S = BSearch(x)
    S.guess_number()
