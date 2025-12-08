from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.user_interaction import user_interaction
from src.vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy(
    "128345474",
    "Системный администратор Linux",
    "Рога и копыта",
    "https://hh.ru/vacancy/128345474",
    "80000 - 120000 руб.",
    "Уметь работать",
)

vacancy_2 = Vacancy(
    "128345475",
    "Системный администратор Linux",
    "Рога и копыта",
    "https://hh.ru/vacancy/128345474",
    "80000 - 120000 руб.",
    "Тоже уметь работать",
)

vacancy_3 = Vacancy(
    "128345476",
    "Системный администратор Linux",
    "Рога и копыта",
    "https://hh.ru/vacancy/128345474",
    "80000 - 120000 руб.",
    "Уметь работать еще лучше",
)

# Сохранение информации о вакансиях в файл

json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.add_vacancy(vacancy_2)
json_saver.add_vacancy(vacancy_3)
json_saver.delete_vacancy(vacancy)  # удаляем из файла vacancy
json_saver.delete_vacancy()  # полностью удаляем все вакансии из файла

# Функция для взаимодействия с пользователем

user_interaction()
