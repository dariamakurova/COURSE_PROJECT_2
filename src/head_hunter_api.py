from src.vacancies_api import VacanciesAPI
import requests
import json

class HeadHunterAPI(VacanciesAPI):
    """ Класс для получения вакансий с платформы HeadHunter"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []



    def _connect(self, keyword: str):
        self.__params['text'] = keyword
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, keyword):
        while self.__params.get('page') != 20:
            vacancies_json = self._connect(keyword)["items"]
            for vacancy in vacancies_json:
                self.__vacancies.append(self._simplify_vacancy(vacancy))
            self.__params['page'] += 1
        return self.__vacancies

    @staticmethod
    def _normalize_salary(value):
        """ Приводит зарплату к рабочему формату """
        if value is None:
            return None
        if isinstance(value, (list, tuple)) and value:
            value = value[0]
        if value == 0:
            return None
        try:
            return int(value)
        except:
            return None


    @classmethod
    def _simplify_vacancy(cls, vacancy):
        salary = vacancy.get("salary", {})
        if salary:
            salary_from = cls._normalize_salary(salary.get("from"))
            salary_to = cls._normalize_salary(salary.get("to"))
            currency = salary.get("currency")
        else:
            salary_from = None
            salary_to = None
            currency = None


        return {
            "id": vacancy.get("id"),
            "name": vacancy.get("name"),
            "url": vacancy.get("url"),
            "salary_from": salary_from,
            "salary_to": salary_to,
            "salary_currency": currency,
            "requirement": vacancy.get("snippet", {}).get("requirement")
        }


if __name__ == "__main__":

    vacancies = HeadHunterAPI()
    print(vacancies.get_vacancies("Python разработчик, Москва"))
