from src.vacancy import Vacancy


def print_vacancies(vacancies: list[Vacancy]):
    """ Печать ключевой информации о вакансии в консоль """
    for vac in vacancies:
        print(vac)

def filter_vacancies(vacancies, keywords: list[str]):
    """ Фильтрация вакансий по ключевым словам """
    if not keywords:
        return vacancies

    filtered_vacs = []
    for vac in vacancies:
        requirement = (vac.requirement or "").lower()
        name = (vac.name or "").lower()
        employer = (vac.employer or "").lower()
        if any(word.lower() in requirement or word.lower() in name or word.lower() in employer for word in keywords):
            filtered_vacs.append(vac)
    return filtered_vacs

def get_vacancies_by_salary(vacancies, salary_range: str):
    """ Получение выкансий в заданном диапозоне зарплат """
    if  not salary_range:
        return vacancies
    try:
        salary_from, salary_to = salary_range.split("-")
        salary_from = int(salary_from.strip()) if salary_from else 0
        salary_to = int(salary_to.strip()) if salary_to else 0
    except ValueError:
        print("Некорректный ввод диапозона зарплат, ожидается формат 0 - 0")
        return vacancies

    if salary_to > 0:
        return [vac for vac in vacancies
            if vac.salary_max >= salary_from and vac.salary_max <= salary_to]
    else:
        return [vac for vac in vacancies
            if vac.salary_max >= salary_from]



def sort_vacancies(vacancies: list[Vacancy]):
    """ Сортирует вакансии по убыванию зарплаты """
    return sorted(vacancies, reverse=True)

def get_top_vacancies(vacancies: list[Vacancy], top=10):
    """ Выводит топ-N вакансий по зарплате """
    return sorted(vacancies, reverse=True)[:top]
