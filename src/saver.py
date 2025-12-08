from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс для работы с файлами - добавление вакансий в файл, получение данных из файла
    по указанным критериям и удаление информации о вакансиях"""

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        """Добавление вакансии в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        """Удаление вакансии"""
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        """Получение вакансий по ключу"""
        pass

    def connect(self):
        pass

    def close(self):
        pass
