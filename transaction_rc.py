import Budget
import Money
from pathlib import Path

paths_for_searching_transaction_rcs = [Path('/etc/transactions/'), Path.home() / 'Transactions/',
                                       Path('transactions/')]


def handle_budget(_budget: Budget.BudgetCategory):
    if _budget.has_transactions():
        print(f'Budget value: {_budget.total}')


def get_list_of_transaction_rcs():
    transaction_choices = []
    for path in paths_for_searching_transaction_rcs:
        transaction_choices += [str(i) for i in path.glob('*')]
    return reversed(transaction_choices)


def parse_transaction_rc(file_name):
    print(f'parsing file "{file_name}"')
    budget = Budget.BudgetCategory()
    for i, line in enumerate(open(file_name).readlines()):
        key, value = line.split(':', 1)
        key = key.strip()
        if key[0:2] == '>>':
            # new budget -- handle previous
            handle_budget(budget)
            budget = Budget.BudgetCategory(value)
        else:
            description = value.strip()
            money = Money.Money(key)
            transaction = Money.Transaction(money, description)
            # TODO: add description & date
            budget.add_transaction(transaction)
    # handle last budget
    handle_budget(budget)
