from fractions import Fraction as F


class Fractran(object):

    def __init__(self, input_state, n):
        self.state = input_state
        self.n = n


    def step(self):

        for s in self.state:
            r = self.n * s
            if r.denominator is 1:
                return r

        return False


    def run(self, steps=100):

        i = 0
        while self.n is not False and i < steps:
            print(self.n)
            self.n = self.step()
            i += 1

        return self.n



if __name__ == "__main__":

    primes = [F(17, 91),
              F(78, 85),
              F(19, 51),
              F(23, 38),
              F(29, 33),
              F(77, 29),
              F(95, 23),
              F(77, 19),
              F(1, 17),
              F(11, 13),
              F(13, 11),
              F(15, 2),
              F(1, 7),
              F(55, 1)]

    f = Fractran(primes, 2)
