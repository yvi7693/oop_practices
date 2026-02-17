
class Car:
    __brand: str
    __model: str
    __release_year: int
    __status: str


    def __init__(self, brand: str, model: str, release_year: int, status: str):
        self.__brand = brand
        self.__model = model
        self.__release_year = release_year
        self.__status = status


    def __str__(self):
        return (f"brand: {self.__brand}"
                f"model: {self.__model}"
                f"release year: {self.__release_year}"
                f"status: {self.__status}")


    def get_brand(self) -> str:
        return self.__brand


    def get_model(self) -> str:
        return self.__model


    def get_release_year(self) -> int:
        return self.__release_year


    def get_status(self) -> str:
        return self.__status


    def set_status(self, new_status: str) -> None:
        self.__status = new_status