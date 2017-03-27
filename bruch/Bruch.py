
class Bruch(object):
    '''
    Bruch überschreibt unzählige standard-Methoedn um sie an Bruchrechnung anzupassen.
    Zum Beispiel :
    - **methods** für brüche:
    * :func:__eq__ : liefert true wenn zähler und nenner gleich sind
    * :func:__abs__ : macht einen negativen bruch positiv
    * :func:__float__ : liefert das Gleitkommaäquivalent zum bruch
    '''
    def __init__(self,zaehler,nenner=None):
        """
        __init__ nimmt als Konstruktor einen zähler und einen nenner, mit dem standard-wert none, entgegen.
        danach wird die Validität der einzelnen Parameter überprüft und gegebenenfalls (nenner = 0, nenner oder zähler ist float)
        eine Exception geworfen. falls nicht 2 int-werte sondern nur 1 bruch objekt übergeben wurde bleibt der nenner none und
        es werden zähler und nenner aus dem objekt eingelesen.
        wird bloß 1 int wert übergeben wird der nenner auf 1 gesetzt (ganze zahl)

        :param zaehler: zähler bzw ganze zahl
        :param nenner:  nenner bzw none
        """
        if nenner == 0:
            raise ZeroDivisionError ("zerodiverr")
        if isinstance(nenner,float) :
            raise TypeError
        if isinstance(zaehler,float):
            raise TypeError
        if (nenner != None):
            self.zaehler = zaehler
            self.nenner = nenner
        elif nenner == None and isinstance(zaehler,int):
            self.zaehler = zaehler
            self.nenner = 1
        else :
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner

    def __eq__(self, other):
        """
        Überschreiben der equals-methode , sodass sie true zurückgibt wenn zähler und nenner eines bruchs gleich sind
        :param other:
        :return: True wenn Zähler und Nenner eines Bruchs gleich sind.
        """
        if isinstance(other,Bruch):
            if(self.zaehler == other.zaehler and self.nenner == other.nenner):
                return True
        else:
            if(float(self) == other):
                return True

    def __float__(self):
        """
        Überschreibt die methode float, sodass sie den Gleitkommawert des Bruchs zurück gibt
        :return: Gleitkommawert des Brcuhs
        """
        floatneu = self.zaehler/self.nenner
        return floatneu

    def __int__(self):
        """
        Überschreibt die methode int, sodass sie den Ganzzahligenwert des Bruchs zurück gibt
        :return: Ganzzahligenwert des Bruchs
        """
        intneu = int(self.zaehler/self.nenner)
        return intneu

    def __complex__(self):
        """
        Überschreibt die Methode complex, sodass complex auf den Gleitkommawert des Bruchs angewendet wird.
        :return:
        """
        complexneu = complex(self.zaehler/self.nenner)
        return complexneu

    def __invert__(self):
        """
        Überschreibt die Methode invert, sodass der Bruch mit vertauschtem Zähler und Nenner zurückgegeben wird
        :return: Bruch(self.nenner,self.zaehler)
        """
        zaehlerneu = self.nenner
        nennerneu = self.zaehler
        return Bruch(zaehlerneu,nennerneu)

    def __str__(self):
        """
        Überschreibt die Methode String, sodass der Bruch in formatierter Form ausgegeben wird. Falls es sich um eine ganze Zahl handelt wird nur der Zähler zurückgegeben.
        :return: Formatierter String des Bruchs
        """
        if(self.nenner == 1):
            return '('+str(self.zaehler)+')'
        else :
            if float(self.zaehler < 0 and self.nenner < 0):
                return str("(" + str(self.zaehler * (-1)) + "/" + str(self.nenner * (-1)) + ")")
            else:
                return str("(" + str(self.zaehler) + "/" + str(self.nenner) + ")")

    def __abs__(self):
        """
        Überschreibt die  Methode abs, sodass ein neuer Bruch mit dem Betrag das alten Nenners und dem Betrag des altern Zählers zurück gegeben wird.
        :return: Neuer Bruch
        """
        zaehlerneu = abs(self.zaehler)
        nennerneu = abs(self.nenner)
        return Bruch(zaehlerneu, nennerneu)

    def __neg__(self):
        """
        Überschreibt die Methode neg, sodass der Bruch invertiert, also mit -1 multipliziert, wird und gibt ihn zurück.
        :return: neuer negierter Bruch
        """
        return(Bruch(self.zaehler*(-1),self.nenner))

    def __pow__(self, power, modulo=None):
        """
        Überschreibt die Methode, sodass der Bruch hoch einer Zahl gehoben wird. Dabei werden je nenner und zähler potenziert
        :param power: potenz
        :param modulo: modulo=None weil kein Modulo benötigt wird
        :return: Bruch hoch der Potenz
        """
        return Bruch(self.zaehler**power,self.nenner**power)

    def _Bruch__makeBruch(value):
        """
        private Methode die einen Bruch über die Eingabe eines einzelnen Wert erstellen lässt. Wirft einen TypeError, falls ein String übergeben wird
        :return: neuen Bruch
        """
        if isinstance(value,str):
            raise TypeError
        else:
            return Bruch(value,value)

    def __add__(self, other):
        """
        Überschreibt die Methode add, sodass ein Bruch zurück gegeben wird der nach den Bruchrechenregeln eine korrekte Summe zweier Brüche darstellt.
        :param other: Bruch der addiert wird
        :return: neuen Bruch = addition von self und other
        """
        if isinstance(other, (float, str)):
            raise TypeError
        other = Bruch(other)
        return Bruch(self.zaehler * other.nenner + other.zaehler * self.nenner, self.nenner * other.nenner)

    def __iadd__(self, other):
        """
        Überschreibt die Methode iadd, sodass es möglich ist den += Operator zu verwenden
        :param other: zweiter Bruch
        :return: neuen Bruch = addition von self und other
        """
        if isinstance(other,(float,str)):
            raise TypeError
        return self + other

    def __radd__(self, other):
        """
        Überschreibt die Methode radd, sodass es möglich ist einen Bruch, konform der Bruchrechenregeln, mit einer ganze Zahl zu multiplizieren
        :param other:
        :return: Bruch multipliziert mit einer ganzen Zahl
        """
        return (Bruch(self.zaehler*other,self.nenner))

    def __truediv__(self, other):
        """
        Überschreibt die Methode div, sodass es möglich ist zwei Brüche, konform der Bruchrechenregeln, durcheinander zu dividieren
        :param other:
        :return: neuer Bruch der durch die Division entstanden ist
        """
        if isinstance(other,(float,str)):
            raise TypeError
        other = Bruch(other)
        return Bruch(self.zaehler*other.nenner, self.nenner*other.zaehler)

    def __rtruediv__(self, other):
        """
        Überschreibt die Methode div, sodass es möglich is einen Bruch, konform der Bruchrechenregeln, durch eine ganze Zahl zu dividieren
        :param other:
        :return:
        """
        if isinstance(other, (float, str)):
            raise TypeError
        other = Bruch(other)
        return Bruch(other.zaehler * self.nenner, other.nenner * self.zaehler)

    def __itruediv__(self, other):
        """
        Überschreibt die Methode itruediv, sodass es möglich ist den =/ Operator  zu verwenden
        :param other:
        :return: Neuer Bruch, Ergebnis der Division self other
        """
        if isinstance(other,(float,str)):
            raise TypeError
        other = Bruch(other)
        return self/other

    def __mul__(self, other):
        """
        Überschreib die Methode mul, sodass es möglich ist 2 Brüche, gemäß der Bruchrechenregeln, zu multiplizieren
        :param other:
        :return: neuer Bruch, Ergebnis der Multiplikation self other
        """
        if isinstance(other,(float,str)):
            raise TypeError
        other = Bruch(other)
        return Bruch(self.zaehler*other.zaehler, self.nenner*other.nenner)

    def __rmul__(self, other):
        """
        Überschreibt die Methode div, sodass es möglich is einen Bruch, konform der Bruchrechenregeln, mit einer ganzen Zahl zu multiplizieren
        :param other:
        :return: neuer Bruch, Ergebnis der Multiplikation
        """
        other = Bruch(other)
        return Bruch(self.zaehler*other.zaehler, self.nenner*other.nenner)

    def __imul__(self, other):
        """
        Überschreibt die Methode itruediv, sodass es möglich ist den *= Operator  zu verwenden
        :param other:
        :return: neuer Bruch, Ergebnis der Multiplikation
        """
        if isinstance(other,(float,str)):
            raise TypeError
        other = Bruch(other)
        return Bruch(self.zaehler*other.zaehler, self.nenner*other.nenner)

    def __sub__(self, other):
        """
        Überschreibt die Methode itruediv, sodass zwei Brüche, gemäß der Bruchrechenregeln, subtrahiert werden können.
        :param other:
        :return: Neuer Bruch, Ergebnis der Subtraktion
        """
        other = Bruch(other)
        bruchselfneu = Bruch(self.zaehler * other.nenner, self.nenner * other.nenner)
        bruchothneu = Bruch(other.zaehler * self.nenner, other.nenner * self.nenner)
        return Bruch(bruchselfneu.zaehler - bruchothneu.zaehler, self.nenner * other.nenner)

    def __isub__(self, other):
        """
        Überschreibt die Methode itruediv, sodass es möglich ist eine ganze Zahl von einem Bruch abzuziehen
        :param other:
        :return: Egebnis der Subtraktion
        """
        if isinstance(other,(float,str)):
            raise TypeError
        other = Bruch(other)
        return self - other

    def __rsub__(self, other):
        """
        Überschreibt die Methode itruediv, sodass es möglich ist den -= Operator  zu verwenden
        :param other:
        :return: Ergebnis der Subtraktion
        """
        if isinstance(other,(float,str)):
            raise TypeError
        other = Bruch(other)
        return other - self

    def __ge__(self, other):
        """
        Überschreibt die Methode ge, sodass 2 Brüche verglichen werden können.
        :param other:
        :return: True wenn gleitkomma self >= gleitkomma other
        """
        if float(self) >= float(other):
            return True

    def __le__(self, other):
        """
        Überschreibt die Methode le, sodass 2 Brüche verglichen werden können.
        :param other:
        :return:True wenn gleitkomma self <= gleitkomma other
        """
        if float(self) <= float(other):
            return True

    def __lt__(self, other):
        """
        Überschreibt die Methode lt, sodass 2 Brüche verglichen werden können.
        :param other:
        :return: True wenn gleitkomma self < gleitkomma other
        """
        if float(self) < float(other):
            return True

    def __gt__(self, other):
        """
        Überschreibt die Methode gt, sodass 2 Brüche verglichen werden können.
        :param other:
        :return: True wenn gleitkomma self > gleitkomma other
        """
        if float(self) > float (other):
            return True

    def __iter__(self):
        """
        Überschreibt die Methode iter, sodass man Brüche in Listen zurückgeben kann.
        :return: Listenelemente
        """

        list = [self.zaehler, self.nenner]
        for x in list:
            yield x