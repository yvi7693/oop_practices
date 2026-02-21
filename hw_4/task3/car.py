from __future__ import annotations

class Car:
    __brand: str
    __model: str
    __price: float
    __release_year: int
    __status: str


    def __init__(self, brand: str, model: str, price: float, release_year: int, status: str):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__release_year = release_year
        self.__status = status


    def __str__(self):
        return (f"brand: {self.__brand}"
                f"model: {self.__model}"
                f"price: {self.__price}"
                f"release year: {self.__release_year}"
                f"status: {self.__status}")


    def get_brand(self) -> str:
        return self.__brand


    def get_model(self) -> str:
        return self.__model


    def get_price(self) -> float:
        return self.__price


    def get_release_year(self) -> int:
        return self.__release_year


    def get_status(self) -> str:
        return self.__status


    def set_price(self, new_price: float) -> None:
        self.__price = new_price


    def set_status(self, new_status: str) -> None:
        self.__status = new_status


    @staticmethod
    def record(original: Car) -> Car:
        return Car(original.__brand, original.__model, original.__price, original.__release_year, original.__status)