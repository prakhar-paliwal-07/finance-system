class Expense:
    def _init_(self, id, description, amount, category, date):
        self.id = id
        self.description=description

        self.amount=amount

        self.category=category
        self.date = date
    def to_dict(self):

        return {"id": self.id,"description": self.description,"amount": self.amount,"category": self.category,"date": self.date}


class Income:

    def _init_(self, id, source, amount, date):
        self.id = id
        
        self.source=source
        self.amount=amount
        self.date=date
    def to_dict(self):
        return {"id": self.id,"source": self.source,"amount": self.amount,"date": self.date}
