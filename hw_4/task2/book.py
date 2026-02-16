from __future__ import annotations


class Book:

    def __init__(self):
        pass


    def __str__(self):
        pass


    def get_tittle(self) -> str:
        pass


    def get_author(self) -> str:
        pass


    def get_year(self) -> int:
        pass


    def get_id(self) -> int:
        pass


    def get_genres(self) -> Genre:
        pass


    def set_year(self, new_year: int) -> None:
        pass


    def add_genre(self, genre: Genre) -> None:
        pass


    def remove_genre(self, genre: Genre) -> None:
        pass




class Genre:

    def __init__(self):
        pass


    def __str__(self):
        pass


    def get_name(self) -> str:
        pass


    def get_description(self) -> str:
        pass


    def set_name(self, new_name: str) -> None:
        pass


    def set_description(self, new_description: str) -> None:
        pass
