from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def final_price(self, price):
        pass


class morning_discount(Strategy):
    def final_price(self, price):
        return round((price - price * 0.25), 2)


class elder_discount(Strategy):
    def final_price(self, price):
        return round((price - price * 0.9), 2)


class Order:
    def __init__(self, price, discount_strategy: Strategy):
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        return self.discount_strategy.final_price(self, self.price)
