"""1․ Գրել Calculator class, որը․
   - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
   - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
   - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
   - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։
"""

# Task 1

class Calculator:
    def __init__(self, num):
        if not (isinstance(num, float) or isinstance(num, int)):
            raise Exception('Error')
        self.__num = num
    def __str__(self):
        return f'Chosen number: {self.__num}'
    def __repr__(self):
        return f'Chosen number: {self.__num} | Type: {type(self.__num)}'

    @property
    def number(self):
        return self.__num

    def __add__(self, other):
        return self.__num + other

    def __radd__(self, other):
        return other + self.__num

    def __sub__(self, other):
        return self.__num - other

    def __rsub__(self, other):
        return other - self.__num

    def __mul__(self, other):
        return self.__num * other

    def __rmul__(self, other):
        return other * self.__num

    def __truediv__(self, other):
        if other == 0:
            raise Exception('Cannot be divided by 0')
        return self / other

    def __rtruediv__(self, other):
        if self.__num == 0:
            raise Exception('Cannot be divided by 0')
        return other / self.__num

    def __floordiv__(self, other):
        if other == 0:
            raise Exception('Cannot be divided by 0')
        return self // other

    def __rfloordiv__(self, other):
        if self.__num == 0:
            raise Exception('Cannot be divided by 0')
        return other // self.__num

    def __mod__(self, other):
        if other == 0:
            raise Exception('Cannot be divided by 0')

    def __rmod__(self, other):
        if self.__num == 0:
            raise Exception('Cannot be divided by 0')
        return other % self.__num

    def __pow__(self, other):
        return self.__num ** other

    def __rpow__(self, other):
        return other ** self.__num
    def __iadd__(self, other):
        self.__num += other
        return self.__num

    def __isub__(self, other):
        self.__num -= other
        return self.__num

    def __imul__(self, other):
        self.__num *= other
        return self.__num

    def __itruediv__(self, other):
        self.__num /= other
        return self.__num

    def __ifloordiv__(self, other):
        self.__num //= other
        return self.__num

    def __imod__(self, other):
        self.__num %= other
        return self.__num

    def __ipow__(self, other):
        self.__num **= other
        return self.__num

    def __eq__(self, other):
        if self.number == other:
            return True
        else:
            return False

    def __ne__(self, other):
        if self != other:
            return True
        else:
            return False

    def __lt__(self, other):
        if self < other:
            return True
        else:
            return False

    def __le__(self, other):
        if self <= other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self > other:
            return True
        else:
            return False

    def __ge__(self, other):
        if self >= other:
            return True
        else:
            return False


c = Calculator(5)
c1 = Calculator(6)
print(c - c1)
print(c1 - c)
print(c)
print(repr(c))
