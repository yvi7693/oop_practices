from hw_4.task3.car import Car
from hw_4.task3.entities import Salesperson, Customer


class Dealership:

    __available: list[Car]
    __salespersons: list[Salesperson]
    __customers: list[Customer]


    def __init__(self, available = [], salesperson = [], customers = []):
        self.__available = available
        self.__salespersons = salesperson
        self.__customers = customers


    def __str__(self):
        return (f"available: {self.get_available()}\n"
                f"salespersons: {self.get_salespersons()}\n"
                f"customers: {self.get_customers()}")


    def shipment(self, car: Car) -> None:
        self.__available.append(car)


    def vend(self, car: Car):
        available = self.__available
        delete_index = None

        for i in range(len(available)):
            if available[i] == car:
                delete_index = i

        if not delete_index is None:
            available.pop(delete_index)


    def lead_generation(self, new_customer: Customer) -> None:
        customers = self.__customers
        is_add = True

        for customer in customers:
            if customer == new_customer:
                is_add = False

        if is_add:
            customers.append(new_customer)


    def hire(self, salesperson: Salesperson) -> None:
        self.__salespersons.append(salesperson)


    def dismiss(self, salesperson: Salesperson) -> None:
        salespersons = self.__salespersons
        delete_index = None

        for i in range(len(salespersons)):
            if salespersons[i] == salesperson:
                delete_index = i

        if not delete_index is None:
            salespersons.pop(delete_index)


    def get_available(self) -> list[str]:
        cars = []

        for car in self.__available:
            cars.append(car.get_brand())

        return cars


    def get_salespersons(self) -> list[str]:
        salespersons = []

        for salesperson in self.__salespersons:
            salespersons.append(salesperson.get_name())

        return salespersons


    def get_customers(self) -> list[Customer]:
        customers = []

        for customer in self.__customers:
            customers.append(customer.get_name())

        return customers