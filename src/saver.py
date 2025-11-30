from abc import ABC, abstractmethod

class Saver(ABC):
    """ Абстрактный класс для работы с файлами - добавление вакансий в файл, получение данных из файла
    по указанным критериям и удаление информации о вакансиях """

    def __init__(self, filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = "vacancies"

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        pass