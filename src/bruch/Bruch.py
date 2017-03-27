'''
    File name: Bruch.py
    Author: Steinwender Jan-Philipp
    Date created: 18/01/2017
    Python Version: 3.4.4
'''

class Bruch(object):
    '''
    :param zaehler: the numerator of the fraction
    :param nenner: the denominator of the fraction
    '''

    def __init__(self, numerator, denominator=1):
        ''' initialize the fraction object

            :param numerator: the numerator of the fraction
            :type numerator: ``int,Bruch``
            :param denominator: the denominator of the fraction
            :type denominator: ``int``
            :raise TypeError: if type is incompatible
            :raise ZeroDivisionError: if division is with zero
        '''
        if isinstance(numerator, Bruch):
            self.zaehler = numerator.zaehler
            self.nenner = numerator.nenner
        elif type(numerator) is int and type(denominator) is int:
            if denominator == 0:
                raise ZeroDivisionError
            self.zaehler = numerator
            self.nenner = denominator
        else:
            raise TypeError

    def __add__(self, other):
        ''' add something to a fraction

            :param other: the number or fraction to add
            :type other: ``int,Bruch``
            :raise TypeError: if type is incompatible
            :return: the new caluclated fraction
        '''
        if isinstance(other, Bruch):
            numerator_new = other.nenner * self.zaehler + self.nenner * other.zaehler
            denominator_new = self.nenner * other.nenner
            return Bruch(numerator_new, denominator_new)
        elif type(other) is int:
            return Bruch((other * self.nenner) + self.zaehler, self.nenner)
        else:
            raise TypeError

    def __radd__(self, other):
        ''' reverse add something to a fraction
            calls the __add__ method

            :param other: the number or fraction to add
            :type other: ``int,Bruch``
            :return: the new caluclated fraction
        '''
        return self.__add__(other)

    def __iadd__(self, other):
        ''' add something in-line to a fraction

            :param other: the number or fraction to add
            :type other: ``int,Bruch``
            :return: the fraction
        '''
        self = self + other
        return self

    def __sub__(self, other):
        ''' subtract something from a fraction

            :param other: the number or fraction to subtract
            :type other: ``int,Bruch``
            :return: the new caluclated fraction
            :raise TypeError: if the value is no integer or a fraction
        '''
        if isinstance(other, Bruch):
            numerator_new = other.nenner * self.zaehler - self.nenner * other.zaehler
            denominator_new = self.nenner * other.nenner
            return Bruch(numerator_new, denominator_new)
        elif type(other) is int:
            return Bruch((self.zaehler - other * self.nenner), self.nenner)
        else:
            raise TypeError

    def __rsub__(self, other):
        ''' reverse subtract something from a fraction

            :param other: the number or fraction to subtract
            :type other: ``int,Bruch``
            :return: the new caluclated fraction
            :raise TypeError: if the value is no integer or a fraction
        '''
        if type(other) is int:
            return Bruch((other * self.nenner - self.zaehler), self.nenner)
        else:
            raise TypeError

    def __isub__(self, other):
        ''' subtract something in-line from a fraction

            :param other: the number or fraction to subtract
            :type other: ``int,Bruch``
            :return: the fraction
        '''
        self = self - other
        return self

    def __mul__(self, other):
        ''' multiply something with a fraction

            :param other: the number or fraction to multiply
            :type other: ``int,Bruch``
            :return: the new caluclated fraction
            :raise TypeError: if the values are not integer or a fraction
        '''
        if isinstance(other, Bruch):
            return float(Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner))
        elif type(other) is int:
            return float(Bruch(self.zaehler * other, self.nenner))
        else:
            raise TypeError

    def __imul__(self, other):
        ''' multiply something in-line with a fraction

            :param other: the number or fraction to multiply
            :type other: ``int,Bruch``
            :return: the fraction
        '''
        self = self * other
        return self

    def __rmul__(self, other):
        ''' reverse multiply something with a fraction

            :param other: the number or fraction to multiply
            :type other: ``int,Bruch``
            :return: the new caluclated fraction
        '''
        return self.__mul__(other)

    def __truediv__(self, other):
        ''' divide something with a number or fraction

            :param other: the number or fraction to divide to
            :type other: ``int,Bruch``
            :return: the new caluclated fraction
            :raise TypeError: if the value is no fraction or int
            :raise ZeroDivisionError: if one of the values are zero
        '''
        if isinstance(other, Bruch):
            if float(other) == 0 or float(self) == 0:
                raise ZeroDivisionError
            return Bruch(self.zaehler * other.nenner, self.nenner * other.zaehler)
        elif type(other) is int:
            if float(other) == 0 or float(self) == 0:
                raise ZeroDivisionError
            return Bruch(self.zaehler, self.nenner * other)
        else:
            raise TypeError

    def __rtruediv__(self, other):
        ''' reverse divide something with a number or fraction

            :param other: the number or fraction to divide to
            :type other: ``int,Bruch``
            :return: the new caluclated fraction
        '''
        return self.__truediv__(other)

    def __itruediv__(self, other):
        ''' divide something in-line with a number or fraction

            :param other: the number or fraction to divide to
            :type other: ``int,Bruch``
            :return: the fraction
        '''
        self = self / other
        return self

    def __float__(self):
        ''' convert a fraction to a float value

            :param other: the fraction
            :type other: ``int,Bruch``
            :return: the float value of the fraction
        '''
        return self.zaehler / self.nenner

    def __eq__(self, other):
        ''' override the equals operator

            :param other: the fraction to compare with
            :type other: ``Bruch``
        '''
        return self.zaehler == other.zaehler and self.nenner == other.nenner

    def __abs__(self):
        ''' override the abs operator
            convert a fraction to an absolute fraction

            :return: the absolute value of the fraction
        '''
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __int__(self):
        ''' override the int operator
            convert a fraction to an integer value

            :return: the int value of the fraction
        '''
        return int(float(self))

    def __neg__(self):
        ''' override the negate operator
            turn a fraction to a negated fraction

            :return: a negative fraction of that fraction
        '''
        return Bruch((-1) * self.zaehler, self.nenner)

    def __invert__(self):
        ''' invert a fraction

        :return: a inverted fraction of that fraction
        '''
        return Bruch(self.nenner, self.zaehler)

    def __pow__(self, power):
        ''' override the exponentiate operator

            :param power: the number to exponentiate the fraction with
            :type other: ``int``
            :raise TypeError: if power is not an integer value
            :return: a exponentiate fraction of the fraction
        '''
        if type(power) is int:
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError

    def __makeBruch(zaehler, nenner=1):
        ''' create a new fraction

            :param zaehler: the numerator
            :type other: ``int``
            :param nenner: the denominator
            :type other: ``int``
            :raise TypeError: if the values are not integer value
            :return: a new fraction
        '''
        if type(zaehler) is int and type(nenner) is int:
            return Bruch(zaehler, nenner)
        else:
            raise TypeError

    def __str__(self):
        ''' convert a fraction to text

        :return: a string represential of the fraction
        '''
        if self.__int__() == self.__float__():
            return "(" + str(self.__int__()) + ")"
        else:
            if self.nenner < 0:
                self.zaehler *= -1
                self.nenner *= -1
            return "(" + str(self.zaehler) + "/" + str(self.nenner) + ")"

    def __ge__(self, other):
        ''' override the greater-equals operator

            :param other: the fraction to compare with
            :type other: ``Bruch``
            :return: if the operation is true or false
        '''
        return self.__float__() >= other.__float__()

    def __gt__(self, other):
        ''' override the greater-than operator

            :param other: the fraction to compare with
            :type other: ``Bruch``
            :return: if the operation is true or false
        '''
        return self.__float__() > other.__float__()

    def __le__(self, other):
        ''' override the less-equals operator

            :param other: the fraction to compare with
            :type other: ``Bruch``
            :return: if the operation is true or false
        '''
        return self.__float__() <= other.__float__()

    def __lt__(self, other):
        ''' override the less-than operator

            :param other: the fraction to compare with
            :type other: ``Bruch``
            :return: if the operation is true or false
        '''
        return self.__float__() < other.__float__()

    def __iter__(self):
        ''' make the fraction class iterable

        :return: a iterable of the class
        '''
        return iter((self.zaehler, self.nenner))
