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