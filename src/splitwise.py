# splitwise.py

class Splitwise:
    def __init__(self):
        self.expenses = []
        self.balances = {}

    def add_expense(self, description, amount, paid_by, participants):
        """
        Add an expense to the system.
        :param description: Description of the expense
        :param amount: Total amount of the expense
        :param paid_by: Person who paid for the expense
        :param participants: List of participants who share the expense
        """
        self.expenses.append({
            'description': description,
            'amount': amount,
            'paid_by': paid_by,
            'participants': participants
        })
        self._update_balances(amount, paid_by, participants)

    def _update_balances(self, amount, paid_by, participants):
        split_amount = amount / len(participants)
        if paid_by not in self.balances:
            self.balances[paid_by] = 0

        # Update balances for the payer
        self.balances[paid_by] += amount - split_amount

        # Update balances for the participants
        for person in participants:
            if person != paid_by:
                if person not in self.balances:
                    self.balances[person] = 0
                self.balances[person] -= split_amount

    def get_balances(self):
        return self.balances

    def print_balances(self):
        print("Balances:")
        for person, balance in self.balances.items():
            print(f"{person}: {'owes' if balance < 0 else 'is owed'} {abs(balance):.2f}")

