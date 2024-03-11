class Customer:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

class Item:
    def __init__(self, name: str, price: int) -> None:
        self.__name = name
        self.__price = price

    def can_be_sold_to():
        return True
    
class AgeRestrictedItem(Item):
    def __init__(self, name: str, price: int) -> None:
        super().__init__(self, name, price)
    
    def can_be_sold_to(age: int):
        if age < 18:
            return False
        return True

class CountryRestrictedItem(Item):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)
    
    def can_be_sold_to(country: str):
        if country == "Arstotzka":
            return False
        return True
        
    
class ShoppingList:
    def __init__(self, owner: Customer):
        self.__owner = owner
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def add(self, item):
        if not item.can_be_sold_to(self.owner):
            raise ValueError()
        self.__items.append(item)
