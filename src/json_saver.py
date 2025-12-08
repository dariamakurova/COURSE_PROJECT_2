import json
import os.path

from src.saver import Saver
from src.vacancy import Vacancy


class JSONSaver(Saver):
    """Класс для работы с JSON файлами вакансий"""

    def __init__(self, path="vacancies.json"):
        self.__filename = os.path.join((os.path.dirname(os.path.dirname(__file__))), "data", path)

        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def _read_file(self):
        with open(self.__filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def _write_file(self, data):
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: dict | Vacancy):
        """Запись вакансий в JSON файл с вакансиями"""

        data = self._read_file()
        id_list = [vac["vac_id"] for vac in data]

        if isinstance(vacancy, dict):
            if vacancy.get("vac_id") not in id_list:
                data.append(vacancy)

        elif isinstance(vacancy, Vacancy):
            vacancy_json = {
                "vac_id": vacancy.vac_id,
                "name": vacancy.name,
                "employer": vacancy.employer,
                "url": vacancy.url,
                "salary": {"from": vacancy.salary_from, "to": vacancy.salary_to, "currency": vacancy.salary_currency},
                "requirement": vacancy.requirement,
            }
            if vacancy_json["vac_id"] not in id_list:
                data.append(vacancy_json)

        self._write_file(data)

    def get_vacancies(self) -> list[Vacancy]:
        """Получает сведения о вакансиях из файла и преобразует в список объектов Vacancy"""
        data = self._read_file()
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
        return vacancies

    def delete_vacancy(self, vacancy: Vacancy = None):
        """Удаляет вакансию по id или полностью очищает файл, если аргумент не передан"""
        data = self._read_file()

        if not vacancy:
            self._write_file([])
            return True
        else:
            vacancy_id = vacancy.vac_id
            updated_data = [vacancy for vacancy in data if vacancy.get("vac_id") != vacancy_id]
            if len(updated_data) == len(data):
                print(f"Вакансия с id {vacancy_id} не найдена")
                return False

            self._write_file(updated_data)
            return True
