from src.vacancies_api import VacanciesAPI
import requests
import json

class HeadHunterAPI(VacanciesAPI):
    """ Класс для получения вакансий с платформы HeadHunter"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100, 'only_with_salary' : True}
        self.__vacancies = []


    def __connect(self, keyword: str):
        """ Метод для подключения к сервису HH по API """
        self.__params['text'] = keyword
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, keyword):
        """ Метод для получения вакансий с HH """
        while self.__params.get('page') != 20:
            vacancies_json = self.__connect(keyword)["items"]
            for vacancy in vacancies_json:
                if vacancy.get("salary") and vacancy.get("salary").get("currency") == "RUR":
                    self.__vacancies.append(self.simplify_vacancy(vacancy))
            self.__params['page'] += 1
        return self.__vacancies


    @classmethod
    def simplify_vacancy(cls, vacancy):
        """ Оставляет только рабочие параметры вакансии """

        return {
            "vac_id": vacancy.get("id"),
            "name": vacancy.get("name"),
            "employer": vacancy.get("employer", {}).get("name"),
            "url": vacancy.get("alternate_url"),
            "salary": vacancy.get("salary"),
            "requirement": vacancy.get("snippet", {}).get("requirement")
        }


if __name__ == "__main__":

    vacancies = HeadHunterAPI()
    print(vacancies.get_vacancies("ТПО ПРАЙД, Москва"))
