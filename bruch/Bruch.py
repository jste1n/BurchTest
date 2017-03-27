class Bruch(object):
    """
    Bruch Klasse
    Stoeger
    23.10.2016
    5BHIT
    """
    def __init__(self, zaehler, nenner=1):
        """ constructor

        :raise TypeError: wrong argument
        :raise ZeroDivisionError:
        :param zaehler: as Bruch or int
        :param nenner: as int (not zero!)
        """
        if type(zaehler) is Bruch:
            self.nenner = zaehler.nenner
            self.zaehler = zaehler.zaehler
        else:
            if type(zaehler) is not int:
                raise TypeError
            if type(nenner) is not int:
                raise TypeError
            if nenner == 0:
                raise ZeroDivisionError
            self.zaehler = zaehler
            self.nenner = nenner

    def __abs__(self):
        """ absolute value

        :return: abs
        """
        if (self.zaehler < 0):
            return Bruch(self.zaehler * (-1), self.nenner)
        else:
            return Bruch(self)

    def __neg__(self):
        """ Negate

        :return: -self
        """
        return Bruch(self.zaehler * (-1), self.nenner)

    def gcd(x, y):
        """ Greatest Common Divisor

        :param x: as int
        :param y: as int
        :return: gcd
        """
        if (abs(x) < abs(y)):
            tmp = abs(x)
        else:
            tmp = abs(y)
        while tmp > 0:
            if (x % tmp == 0) & (y % tmp == 0):
                return tmp
            tmp -= 1

    def __repr__(self):
        """ Determines how this object is representated as string

        :return: str
        """
        shorten = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler //= shorten
        self.nenner //= shorten
        # Minus in den Zaehler
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __makeBruch(other):
        """ Creates a new Bruch out of an int or another Bruch

        :return: Bruch
        """
        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError

    def __eq__(self, other):
        """ Equal to

        :param Bruch:
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return float(self) == float(other)

    def __ne__(self, other):
        """ Not Equal to

        :param Bruch:
        :return: boolean
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """ Greather Than

        :param Bruch:
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner > other.zaehler * self.nenner

    def __lt__(self, other):
        """ Lower Than

        :param Bruch:
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner < other.zaehler * self.nenner

    def __ge__(self, other):
        """ Greather or Equal to
        :param Bruch:
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner >= other.zaehler * self.nenner

    def __le__(self, other):
        """ Lower or Equal to
        :param Bruch:
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner <= other.zaehler * self.nenner

    def __float__(self):
        """ overrides float()

        :return: float
        """
        return float(self.zaehler / self.nenner)

    def __int__(self):
        """ overrides int()

        :return: int
        """
        return int(self.__float__())

    def __radd__(self, zaehler):
        """ right version of add

        :raise TypeError:
        :param zaehler: as int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler)

    def __add__(self, zaehler):
        """ addition

        :raise TypeError:
        :param zaehler: as int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            zaehler2, nenner2 = zaehler
        elif type(zaehler) is int:
            zaehler2, nenner2 = zaehler, 1
        else:
            raise TypeError
        nennerNeu = self.nenner * nenner2
        zaehlerNeu = zaehler2 * self.nenner + nenner2 * self.zaehler
        return Bruch(zaehlerNeu, nennerNeu)

    def __complex__(self):
        """ overrides complex()

        :return: complex
        """
        return complex(self.__float__())

    def __rsub__(self, left):
        """ right version of substract

        :raise TypeError:
        :param zaehler: as int
        :return: Bruch
        """
        if type(left) is int:
            zaehler2 = left
            nennerNeu = self.nenner
            zaehlerNeu = zaehler2 * self.nenner - self.zaehler
            return Bruch(zaehlerNeu, nennerNeu)
        else:
            raise TypeError

    def __sub__(self, zaehler):
        """ subtraction

        :raise TypeError:
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler * -1)

    def __rmul__(self, zaehler):
        """ right version of multiplication

        :raise TypeError:
        :param zaehler: as int or Bruch
        :return: Bruch
        """
        return self.__mul__(zaehler)

    def __mul__(self, zaehler):
        """ multiplication

        :raise TypeError:
        :param zaehler: as int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            zaehler2, nenner2 = zaehler
        elif type(zaehler) is int:
            zaehler2, nenner2 = zaehler, 1
        else:
            raise TypeError
        zaehler2 *= self.zaehler
        nenner2 *= self.nenner
        return Bruch(zaehler2, nenner2)

    def __pow__(self, power):
        """ Bruch power to self

        :raise TypeError:
        :param power: as int
        :return: Bruch
        """
        if type(power) is int:
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError

    def __rtruediv__(self, left):
        """ division

        :raise TypeError:
        :param zaehler: as int
        :return: Bruch
        """
        if type(left) is int:
            newzaehler = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(newzaehler, self.zaehler)
        else:
            raise TypeError

    def __truediv__(self, zaehler):
        """ division

        :raise TypeError:
        :param zaehler: as Bruch or int
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            zaehler2, nenner2 = zaehler
        elif type(zaehler) is int:
            zaehler2, nenner2 = zaehler, 1
        else:
            raise TypeError
        if zaehler2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(nenner2, zaehler2))

    def __invert__(self):
        """ invert Bruch

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __iter__(self):
        """
        iterable
        """
        return (self.zaehler, self.nenner).__iter__()

    def __iadd__(self, other):
        """ intern addition

        :param Bruch: as Bruch or int
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self + other
        return self

    def __isub__(self, other):
        """ intern subtraction

        :param Bruch: as Bruch or int
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self - other
        return self

    def __imul__(self, other):
        """ intern muliplication

        :param Bruch: as Bruch or int
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self * other
        return self

    def __itruediv__(self, other):
        """ intern division

        :param Bruch: as Bruch or int
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self / other
        return self
