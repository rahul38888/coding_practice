class Product:
    def __init__(self, name: str, price: int):
        self.__name = name
        self.__price = price

    def p_name(self) -> str:
        return self.__name

    def price(self) -> int:
        return self.__price

    def __hash__(self):
        return hash((self.__name, self.__price))

    def __eq__(self, other):
        if type(other) is not Product:
            return False

        if self.__name == other.__name and self.__price == other.__cost:
            return True

        return False


class Biscuit(Product):
    def __int__(self):
        super().__init__("biscuit", price=12)


class Cake(Product):
    def __int__(self):
        super().__init__("cake", price=12)


class Sandwich(Product):
    def __int__(self):
        super().__init__("sandwich", price=12)


class Transaction:
    def __init__(self, product: Product, money: dict[int: int]):
        self._product = product
        self._money = money

    def get_product(self) -> Product:
        return self._product


class PurchaseInput(Transaction):
    def __init__(self, product: Product, money: dict[int: int]):
        super().__init__(product, money)

    def get_money(self) -> dict[int: int]:
        return self._money


class PurchaseOutput(Transaction):
    def __init__(self, product: Product, change: dict[int: int]):
        super().__init__(product, change)

    def get_change(self) -> dict[int: int]:
        return self._money


class VendingMachine:
    def __init__(self, max_space: int):
        self.__max__space = max_space
        self.__stock: list[Product] = list()
        self.__money: dict[int: int] = dict()

    def stock_report(self):
        pass

    def restock(self, products: list[Product]):
        pass

    def collect_all_money(self, amount: int):
        pass

    def get_product(self, product: Product):
        pass


class MyVendingMachine(VendingMachine):
    def __init__(self, max_space: int):
        super().__init__(max_space)

    def stock_report(self):
        stock_map = dict()
        for p in self.__stock:
            if not stock_map.__contains__(p):
                stock_map[p] = 0
            stock_map += 1
        return stock_map

    def __empty_space(self) -> int:
        return self.__max__space - len(self.__stock)

    def __add_product(self, product: Product):
        if self.__empty_space():
            self.__stock.append(product)

    def restock(self, products: list[Product]) -> list[Product]:
        empty_space = self.__empty_space()
        if empty_space:
            for _ in range(empty_space):
                product = products.pop(0)
                self.__add_product(product)

        return products

    def __has_currency(self, currency: int):
        return self.__money.__contains__(currency) and self.__money[currency]

    def __remove_currency(self, currency: int) -> bool:
        if self.__has_currency(currency):
            self.__money[currency] -= 1
            return True
        return False

    def collect_money(self, amount: int, more_allowed: bool) -> dict[int: int]:
        currencies = list(self.__money.keys())
        currencies.sort()
        note_index = len(currencies) - 1
        collection: dict[int: int] = dict()
        while amount > 0 and note_index >= 0:
            currency = currencies[note_index]
            if (amount < currency or not self.__has_currency(currency)) and self.__remove_currency(currency):
                note_index += 1
                continue
            if not collection.__contains__(currency):
                collection[currency] = 0
            collection[currency] += 1
            amount -= currency

        if amount > 0:
            if not more_allowed:
                return None

            i = 0
            while i < len(currencies):
                currency = currencies[i]
                if amount < currency:
                    if not collection.__contains__(currency):
                        collection[currency] = 0
                    collection[currency] += 1
                    break







