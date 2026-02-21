from __future__ import annotations

from hw_4.task2.model.book import Book
from hw_4.task2.model.employee import Employee


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
        return (f"name: {self.__name}"
                f"address: {self.__address}"
                f"books: {self.__books}"
                f"employees: {self.__employees}")


    def get_name(self) -> str:
        return self.__name


    def get_books(self) -> list[Book]:
        record_books = []

        for book in self.__books:
            record_books.append(Book.record(book))

        return record_books


    def get_employees(self) -> list[Employee]:
        record_employees = []

        for employee in self.__employees:
            record_employees.append(Employee.record(employee))

        return record_employees


    def set_address(self, new_address: str) -> None:
        self.__address = new_address