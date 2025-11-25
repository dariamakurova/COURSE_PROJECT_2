from abc import ABC, abstractmethod

class VacanciesAPI(ABC):
    """ Абстрактный класс для получения вакансий по API """

    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, *args, **kwargs):
        """ Загрузка вакансий с платформы"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """ Получение текущего списка вакансий """
        pass

    @abstractmethod
    def save(self):
        """ Сохранение вакансий в файл """
        pass