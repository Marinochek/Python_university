# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        if not isinstance(make, str):
            raise TypeError("Производитель должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("Год должен быть целым числом и не меньше 1886")

        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        ...

    def stop_engine(self) -> None:
        ...

    def get_vehicle_info(self) -> str:
        return f"{self.make} {self.model}, {self.year}"


class Computer:
    def __init__(self, brand: str, ram: int, storage: int):
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(ram, int) or ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным целым")
        if not isinstance(storage, int) or storage <= 0:
            raise ValueError("Объем накопителя должен быть положительным целым")

        self.brand = brand
        self.ram = ram
        self.storage = storage

    def upgrade_ram(self, additional_ram: int) -> None:
        if not isinstance(additional_ram, int) or additional_ram <= 0:
            raise ValueError("Объем добавляемой оперативной памяти должен быть положительным целым")
        self.ram += additional_ram

    def get_computer_info(self) -> str:
        return f"{self.brand}, RAM: {self.ram}GB, Storage: {self.storage}GB"


class Book:
    def __init__(self, title: str, author: str, pages: int):
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int) -> None:
        if not isinstance(pages_to_read, int) or pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным целым")
        if pages_to_read > self.pages:
            raise ValueError("Нельзя прочитать больше страниц, чем есть в книге")

    def get_book_info(self) -> str:
        return f"{self.title} by {self.author}, {self.pages} pages"

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
