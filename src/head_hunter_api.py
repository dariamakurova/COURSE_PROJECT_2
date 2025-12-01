from src.vacancies_api import VacanciesAPI
import requests
import json

class HeadHunterAPI(VacanciesAPI):
    """ Класс для получения вакансий с платформы HeadHunter"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies_json = response.json()['items']

            for vacancy in vacancies_json:
                self.vacancies.append(self._simplify_vacancy(vacancy))

            self.params['page'] += 1
        return self.vacancies

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
