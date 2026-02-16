from __future__ import annotations
class Library:

    __name: str
    __address: str
    __books: list[Book]
    __employees: list[Employee]


    def __init__(self, name: str, address: str, books: list[Book], employees: list[Employee]):
        self.__name = name
        self.__address = address
        self.__books = books
        self.__employees = employees


    def __str__(self):
        pass


    def get_name(self) -> str:
        pass


    def get_books(self) -> list[Book]:
        pass


    def get_employees(self) -> list[Employee]:
        pass


    def set_address(self, new_address: str) -> None:
        self.__address = new_address