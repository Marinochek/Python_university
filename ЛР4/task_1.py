import doctest

class Book:
    """Базовый класс книги."""

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге
        :raises TypeError: Если title или author не строка, или pages не целое число
        :raises ValueError: Если pages меньше или равно нулю
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым")

        self.title = title
        self.author = author
        self._pages = pages  # Приватный атрибут для хранения количества страниц, чтобы предотвратить прямое изменение извне



    def __str__(self) -> str:
        """Строковое представление книги"""
        return f"Книга '{self.title}' автор {self.author}, {self._pages} страниц"

    def __repr__(self) -> str:
        """Представление объекта книги"""
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self._pages})"

    def get_info(self) -> str:
        """
        Получить информацию о книге

        :return: Строка с информацией о книге
        """
        return f"{self.title} by {self.author}, {self._pages} pages."


class PaperBook(Book):
    """Класс для бумажной книги, наследуется от Book."""

    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Инициализация бумажной книги.

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге
        """
        super().__init__(title, author, pages)

    def __str__(self) -> str:
        """Строковое представление бумажной книги, добавляющее информацию о типе книги."""
        return f"[Бумажная книга] {super().__str__()}"

    def turn_page(self, pages: int) -> str:
        """
        Перевернуть указанные страницы.

        :param pages: Количество страниц для переворачивания
        :return: Информация о переворачивании страниц
        :raises ValueError: Если количество страниц меньше или равно нулю
        """
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц для переворачивания должно быть положительным целым")
        return f"Перевернуто {pages} страниц(ы) в книге '{self.title}'."

    def __repr__(self) -> str:
        """Представление объекта бумажной книги."""
        return f"PaperBook(title={self.title!r}, author={self.author!r}, pages={self._pages})"

    def get_info(self) -> str:
        """
        Получить информацию о бумажной книге в специфическом формате.

        :return: Строка с информацией о бумажной книге
        Это позволяет использовать форматированную строку для получения информации,
        которая более читабельна и понятна для пользователя конкретного типа книги.
        """
        return f"[Бумажная книга] {self.title} (автор: {self.author}), {self._pages} страниц"


class AudioBook(Book):
    """Класс для аудиокниги, наследуется от Book."""

    def __init__(self, title: str, author: str, duration: float) -> None:
        """
        Инициализация аудиокниги.

        :param title: Название книги
        :param author: Автор книги
        :param duration: Длительность аудиокниги в часах
        :raises TypeError: Если duration не число (float)
        :raises ValueError: Если duration меньше или равно нулю
        """
        super().__init__(title, author, 0)  # Устанавливаем страницы в 0, для аудиокниги
        if not isinstance(duration, (int, float)):
            raise TypeError("Длительность должна быть числом (int или float).")
        if duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.duration = duration

    def __str__(self) -> str:
        """Строковое представление аудиокниги, добавляющее информацию о типе книги"""
        return f"[Аудиокнига] {self.title} автор {self.author}, длительность {self.duration} часов"

    def listen(self, time: float) -> str:
        """
        Прослушать определенное время аудиокниги.

        :param time: Время прослушивания в часах
        :return: Информация о прослушивании
        :raises ValueError: Если время меньше или равно нулю
        """
        if time <= 0:
            raise ValueError("Время прослушивания должно быть положительным числом")
        return f"Вы прослушали {time} час(а/ов) аудиокниги '{self.title}'"

    def __repr__(self) -> str:
        """Представление объекта аудиокниги."""
        return f"AudioBook(title={self.title!r}, author={self.author!r}, duration={self.duration})"

    def get_info(self) -> str:
        """
        Получить информацию об аудиокниге в специфическом формате.

        :return: Строка с информацией об аудиокниге
        Выделяет особую информацию о длительности и формате аудиокниги.
        """
        return f"[Аудиокнига] {self.title} (автор: {self.author}), длительность {self.duration} часов"


def test() -> None:
    """
    Тесты для проверки работы классов.

    >>> paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    >>> paper_book.get_info()
    '[Бумажная книга] Война и мир (автор: Лев Толстой), 1225 страниц'

    >>> audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)
    >>> audio_book.get_info()
    '[Аудиокнига] 1984 (автор: Джордж Оруэлл), длительность 11.5 часов'

    >>> paper_book.turn_page(10)
    "Перевернуто 10 страниц(ы) в книге 'Война и мир'."

    >>> audio_book.listen(1)
    "Вы прослушали 1 час(а/ов) аудиокниги '1984'"
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

    print(paper_book)  # Проверяем метод __str__
    print(audio_book)  # Проверяем метод __str__

    print(paper_book.turn_page(10))  # Проверяем метод turn_page
    print(audio_book.listen(1))  # Проверяем метод listen

    test()  # Запускаем тесты
