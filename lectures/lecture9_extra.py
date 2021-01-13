import math


class Rational:
    def __init__(self, n, d=1):
        if d == 0:
            raise ZeroDivisionError("denom must be non-zero")
        divisor = math.gcd(n, d)
        # there are shorter ways to implement sign, but this is more readable
        self.is_negative = (n < 0 < d) or (d < 0 < n)
        self.numer = abs(n) // divisor
        self.denom = abs(d) // divisor

    def __repr__(self):
        s = f"{self.numer}/{self.denom}"
        if self.is_negative:
            s = "-" + s
        return s

    # should be a static method, but this is beyond the scope of this course
    def convert_other(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return other

    def __add__(self, other):
        other = self.convert_other(other)
        # needs to be refferred with is_negative taken to account
        print(other.numer)
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Rational(-self.numer, self.denom)

    def __sub__(self, other):
        return self + (-other)

    # we can also implement floordiv, rmul, rtruediv ect.
    def __mul__(self, other):
        other = self.convert_other(other)
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        other = self.convert_other(other)
        return self * Rational(other.denom, other.numer)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __lt__(self, other):
        if (not self.is_negative and not other.is_negative) or (self.is_negative and other.is_negative):
            return (self.numer * other.denom) < (other.numer * self.denom)
        else:
            return (self.numer * other.denom) > (other.numer * self.denom)

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)


r1 = Rational(2, 2)
r2 = Rational(2, 2)
print(r1-r2)
