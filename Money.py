import typing

from Date import Date


class Money:
    _string: str = None
    _value: float = 0
    # TODO: determine default currency from locale
    _currency: str = 'USD'

    def __init__(self, value: typing.Union[str, float] = None) -> None:
        if value is None:
            pass
        elif isinstance(value, str):
            self.string_to_money(value, self)
        elif isinstance(value, float) or isinstance(value, int):
            self.set_value(value)
        else:
            raise ValueError

    def set_value(self, money_value: float):
        self._value = money_value

    def get_currency(self):
        return self._currency

    def get_value(self):
        return self._value

    def set_currency(self, currency: str):
        self._currency = currency

    def __str__(self):
        return f"{self._value} {self._currency}"

    def __float__(self):
        return self._value

    def __add__(self, other):
        return self._value + self.normalize(other)

    def __sub__(self, other):
        return self._value - self.normalize(other)

    def __eq__(self, other: str):
        return self._value == self.normalize(other)

    def __ne__(self, other):
        return self._value != self.normalize(other)

    __radd__ = __add__
    __rsub__ = __sub__

    @staticmethod
    def normalize(other) -> float:
        if isinstance(other, float):
            return other
        elif isinstance(other, str):
            return Money(other).get_value()

    @staticmethod
    def string_to_money(money_string: str, money_obj):
        money_obj._string = money_string.strip()
        try:
            value, currency = money_obj._string.split(' ')
            money_obj._value = float(value)
            money_obj._currency = currency
        except ValueError:
            money_obj._value = float(money_obj._string)


class Transaction:
    _amount: Money
    _description: str = 0
    _date: Date

    def __init__(self, amount: Money = Money, description: str = '', date: Date = Date):
        self._amount = amount
        self._description = description
        self._date = date

    def __int__(self):
        return int(self._amount)

    def __float__(self):
        return float(self._amount)

    @property
    def amount(self):
        return self._amount

