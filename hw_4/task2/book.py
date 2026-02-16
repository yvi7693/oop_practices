from __future__ import annotations


class Book:

    tittle: str
    author: str
    year: int
    id: int
    genres: list[Genre]


    def __init__(self, tittle: str, author: str, year: int, id: int, genres: list[Genre]):
        self.__tittle = tittle
        self.__author = author
        self.__year = year
        self.__id = id
        self.__genres = genres


    def __str__(self):
        return (f"tittle: {self.__tittle}"
                f"author: {self.__author}"
                f"year: {self.__year}"
                f"id: {self.__id}"
                f"genres: {self.__genres}")


    def get_tittle(self) -> str:
        return self.__tittle


    def get_author(self) -> str:
        return self.__author


    def get_year(self) -> int:
        return self.__year


    def get_id(self) -> int:
        return self.__id


    def get_genres(self) -> list[Genre]:
        return self.__genres


    def set_year(self, new_year: int) -> None:
        self.__year = new_year


    def add_genre(self, new_genre: Genre) -> None:
        is_may = True

        for genre in self.__genres:
            if genre == new_genre:
                is_may = False

        if is_may:
            self.__genres.append(new_genre)



    def remove_genre(self, genre_delete: Genre) -> None:
        genres = self.__genres
        delete_index = None

        for i in range(len(genres)):
            if genres[i] == genre_delete:
                delete_index = i

        if not delete_index is None:
            genres.pop(delete_index)




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
