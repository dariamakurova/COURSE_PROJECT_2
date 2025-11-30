from mypy.config_parser import str_or_array_as_list


class Vacancy():
    """ Класс для вакансий """

    def __init__(self, name, url, salary_from=None, salary_to=None, requirement=""):
        if not name or not isinstance(name, str):
            self.name = "Без названия"
        else:
            self.name = name

        if not url or not isinstance(url, str) or not url.startswith("http"):
            self.url = "Ссылка не указана"
        else:
            self.url = url

        if isinstance(salary_from, dict) and salary_to is None:
            salary_to = salary_from.get('to')
            salary_from = salary_from.get('from')

        s_from = salary_from if isinstance(salary_from, (int, float)) else None
        s_to = salary_to if isinstance(salary_to, (int, float)) else None

        s_from = max(0, s_from) if s_from is not None else 0
        s_to = max(0, s_to) if s_to is not None else 0

        self.salary_from = s_from
        self.salary_to = s_to

        self.salary = max(self.salary_from, self.salary_to)

        self.requirement = requirement or ""


    def __lt__(self, other):
        """ Метод для операции сравнения «меньше» """
        return self.salary < other.salay

    def __le__(self, other):
        """ Метод для операции сравнения «меньше или равно» """
        return self.salary <= other.salary

    def __gt__(self, other):
        """ метод для операции сравнения «больше» """
        return self.salary > other.salay

    def __ge__(self, other):
        """ Метод для операции сравнения «больше или равно» """
        return self.salary >= other.salary
