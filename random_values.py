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

    def _postconditions(self, list_of_random, amount, min_range, max_range):
        # Postconditions:
        # First checks that the correct amount of variables have been appended
        if len(list_of_random) != amount:
            raise Exception("List recieved incorrect amount of values")
        # Second checks that the appended values are within the given range
        for rand_int in list_of_random:
            if rand_int < min_range or rand_int > max_range:
                raise Exception("Random number is outside of the given range")

    def random_nums(self, amount: int, min_range: int, max_range: int):
        """
        Takes the parameters amount, minRange, maxRange.
        Then returns values equal to the amount and in the range of
        minRange to maxRange.

        :return:
        list of int
        """

        # Calls the preconditions method and passes the correct parameters
        self._preconditions(amount, min_range, max_range)

        list_of_random = []
        for i in range(amount):
            value = random.randint(min_range, max_range)
            list_of_random.append(value)

        # Calls the postconditions method and passes the correct parameters
        self._postconditions(list_of_random, amount, min_range, max_range)

        return list_of_random


# Example test code
rando = Randomizer()
print(rando.random_nums(4, 4, 30))
print(rando.random_nums(2, 4, 30))
