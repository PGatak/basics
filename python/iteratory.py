class IncrementIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        return self.i


print([a for a in IncrementIterator(10)])


class FizzBuzzIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        if not self.i % 3:
            return 'Fizz'
        elif not self.i % 5:
            return 'Buzz'
        else:
            return self.i


print([a for a in FizzBuzzIterator(10)])
