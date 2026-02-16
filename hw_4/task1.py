from __future__ import annotations


# task1

class Student:

    __first_name: str
    __last_name: str
    __average_score: float

    def __init__(self, first_name: str, last_name: str, average_ball: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__average_score = average_ball


    def __str__(self):
        return (f"first name: {self.__first_name}"
                f"last name: {self.__last_name}"
                f"average ball: {self.__average_score}")


    def __eq__(self, other: Student):
        return self.__average_score == other.average_score


    def __ne__(self, other: Student):
        return self.__average_score != other.average_score


    def __lt__(self, other: Student):
        return self.__average_score < other.average_score


    def __gt__(self, other: Student):
        return self.__average_score > other.average_score


    def __le__(self, other: Student):
        return self.__average_score <= other.average_score


    def __ge__(self, other: Student):
        return self.__average_score >= other.average_score


    def get_first_name(self) -> str:
        return self.__first_name


    def get_last_name(self) -> str:
        return self.__last_name


    def __get_average_score(self) -> float:
        return self.__average_score


    def set_first_name(self, new_name: str) -> None:
        self.__first_name = new_name


    def set_last_name(self, new_name: str) -> None:
        self.__last_name = new_name


    def __set_average_score(self, new_average_score: float) -> None:
        self.__average_score = new_average_score

    average_score = property(__get_average_score, __set_average_score)



bob = Student("Bob", "Ba", 4.5)
bib = Student("Bib", "Ba", 4.3)

print(bob == bib)
print(bob != bib)
print(bob > bib)
print(bob < bib)
print(bob >= bib)
print(bob <= bib)
