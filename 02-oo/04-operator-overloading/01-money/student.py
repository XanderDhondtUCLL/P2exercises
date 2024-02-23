class Money :
    def __init__(self, amount:int, currency:str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            raise RuntimeError("Mismatched currencies!")
        return (self.amount + other.amount)
        
    def __sub__(self, other):
        if self.currency == other.currency:
            raise RuntimeError
        return (self.amount - other.amount)
        
    def __mul__(self, value):
        return (self.amount * value, self.currency)