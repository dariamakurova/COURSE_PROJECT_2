import json
import os.path

from src.saver import Saver

class JSONSaver(Saver):
    """ Класс для работы с JSON файлами вакансий"""

    def __init__(self, filename="vacancies.json"):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def _read_file(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return json.load(file)


    def _write_file(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def add_vacancy(self, vacancy: dict):
        """ Добавление вакансии """
        data = self._read_file()
        data.append(vacancy)
        self._write_file(data)


    def get_vacancies(self, **parameter):
        """ Возвращает вакансии по заданным параметрам """
        data = self._read_file()
        for key, value in parameter.items():
            data = [vacancy for vacancy in data if vacancy.get(key) == value]

        return data

    def delete_vacancy(self, vacancy_id):
        """ Удаляет вакансию по id """
        data = self._read_file()

        updated_data = [vacancy for vacancy in data if vacancy.get("id") != vacancy_id]
        if len(updated_data) == len(data):
            print(f"Вакансия с id {vacancy_id} не найдена")
            return False

        self._write_file(updated_data)
        return True
