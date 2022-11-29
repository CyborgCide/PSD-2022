import random


class Randomizer:
    """A class featuring a method for randomization of numbers"""

    def _preconditions(self, amount, minRange, maxRange):
        # Preconditions making sure the parameter values are valid:
        # First checks that the minRange is smaller than the maxRange to
        # avoid errors when computing.
        if minRange > maxRange:
            raise ValueError("minRange cannot be larger than maxRange")
        # Second checks that the amount variable is a positive number
        elif amount <= 0:
            raise ValueError("Amount variable must be greater than 0")

    def random_nums(self, amount: int, minRange: int, maxRange: int):
        """
        Takes the parameters amount, minRange, maxRange.
        Then returns values equal to the amount and in the range of
        minRange to maxRange.

        :return:
        list of int
        """

        self._preconditions(amount, minRange, maxRange)

        list_of_random = []
        for i in range(amount):
            value = random.randint(minRange, maxRange)
            list_of_random.append(value)

        # Postconditions:
        # First checks that the correct amount of variables have been appended
        if len(list_of_random) != amount:
            raise Exception("Error when appending")
        # Second checks that the appended values are within the given range
        for rand_int in list_of_random:
            if rand_int < minRange or rand_int > maxRange:
                raise Exception("Random number is outside of the given range")

        return list_of_random


# Example test code
rando = Randomizer()
print(rando.random_nums(0, 4, 30))
print(rando.random_nums(2, 4, 30))
