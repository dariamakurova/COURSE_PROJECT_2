from abc import ABC, abstractmethod

class VacanciesAPI(ABC):
    """ Абстрактный класс для получения вакансий по API """

    def get_vacancies(self):
        pass