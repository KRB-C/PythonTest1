class BSearch:  # Simple Binary Search from 0 - 100
    def __init__(self, guess_num, num_max=100):
        self.guess = 0  # number of guesses before finding correct number
        self.min = 0
        self.max = num_max
        self.to_guess = guess_num  # Number to Guess
        self.cur_guess = (self.max + self.min) // 2  # Current Guess number
        print(f"Your current number is {self.to_guess}")

    def new_guess(self):
        self.cur_guess = (self.max + self.min) // 2
        return

    def guess_number(self):
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
                f"Number of Guesses before finding the number is {self.guess} \n")


S = BSearch(22, 30)
S.guess_number()
