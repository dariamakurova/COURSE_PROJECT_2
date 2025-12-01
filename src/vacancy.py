from mypy.config_parser import str_or_array_as_list


class Vacancy():
    """ Класс для вакансий """

    def __init__(self, id, name, url, salary_from=None, salary_to=None, requirement=""):

        self.id = id

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
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        else:
            raise TypeError

    def __le__(self, other):
        """ Метод для операции сравнения «меньше или равно» """
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        else:
            raise TypeError

    def __gt__(self, other):
        """ метод для операции сравнения «больше» """
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        else:
            raise TypeError

    def __ge__(self, other):
        """ Метод для операции сравнения «больше или равно» """
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        else:
            raise TypeError


    @classmethod
    def cast_to_object_list(cls, vacancies_json):
        vacancies = []
        for vacancy in vacancies_json:
            obj = cls(id=vacancy.get("id"),
                      name=vacancy.get("name"),
                      url=vacancy.get("url"),
                      salary_from=vacancy.get("salary_from"),
                      salary_to=vacancy.get("salary_to"),
                      requirement=vacancy.get("requirement"))
            vacancies.append(obj)
        return vacancies