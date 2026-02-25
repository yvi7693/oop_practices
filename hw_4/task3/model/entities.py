from __future__ import annotations
from hw_4.task3.model.car import Car

class Customer:

    __name: str
    __phone: int
    __email: str
    __orders: list[Car]

    def __init__(self, name: str, phone: int, email: str, ordered_car = []):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__ordered_cars = ordered_car

    def get_name(self) -> str:
        return self.__name


    def get_phone(self) -> int:
        return self.__phone


    def get_email(self) -> str:
        return self.__email


    def set_phone(self, new_phone: int) -> None:
        self.__phone = new_phone


    def set_email(self, new_email: str) -> None:
        self.__email = new_email


    def buy(self, car: Car) -> None:
        self.__ordered_cars.append(car)


    def refund(self, refund_car: Car) -> None:
        orders = self.__ordered_cars
        delete_index = None

        for i in range(len(orders)):
            if orders[i] == refund_car:
                delete_index = i

        if not delete_index is None:
            orders.pop(delete_index)


    @staticmethod
    def record(original: Customer) -> Customer:
        return Customer(original.__name, original.__phone, original.__email, original.__orders)



class Salesperson:

    __name: str
    __experience: int
    __sales: list[Car]

    def __init__(self, name: str, experience: int, sales = []):
        self.__name = name
        self.__experience = experience
        self.__sales = sales


    def vend(self, car: Car) -> None:
        self.__sales.append(car)


    def delete_car(self, delete_car: Car) -> None:
        sales = self.__sales
        delete_index = None

        for i in range(len(sales)):
            if sales[i] == delete_car:
                delete_index = i

        if not delete_index is None:
            sales.pop(delete_index)

    def get_name(self) -> str:
        return self.__name


    def get_experience(self) -> int:
        return self.__experience


    def get_sales(self) -> list[str]:
        sales = []

        for sale in self.__sales:
            sales.append(sale.get_brand())

        return sales


    def build_experience(self, year: int) -> None:
        self.__experience += year


    @staticmethod
    def record(original: Salesperson) -> Salesperson:
        return Salesperson(original.__name, original.__experience, original.__sales)