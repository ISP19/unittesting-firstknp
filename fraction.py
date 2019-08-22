import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        gcd = math.gcd(numerator, denominator)
        self.numerator = int(numerator/gcd)
        self.denominator = int(denominator/gcd)
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d
        """
        return Fraction((self.numerator * frac.denominator) + (frac.numerator * self.denominator), (self.denominator * frac.denominator))

    def __sub__(self, frac):
        return Fraction((self.numerator * frac.denominator) - (frac.numerator * self.denominator), (self.denominator * frac.denominator))

    def __mul__(self, frac):
        return Fraction((self.numerator * frac.numerator), (self.denominator * frac.denominator))

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + '/' + str(self.denominator)



if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
