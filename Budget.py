from typing import List

from Date import Date
from Money import Money, Transaction


class BudgetCategory:
    _allotment: Money = 0
    _transactions: List[Transaction] = []
    _total: Money = 0

    def __init__(self, _allotment: Money = 0):
        self._allotment = _allotment
        self._total = _allotment

    def has_transactions(self) -> bool:
        return len(self._transactions) > 0

    def add_transaction(self, transaction=Transaction, money=Money, date=Date, description=''):
        if transaction == 0:
            transaction = Transaction(money, date, description)
        self._transactions.append(transaction)
        self._total += transaction.amount

    @property
    def total(self):
        return self._total
