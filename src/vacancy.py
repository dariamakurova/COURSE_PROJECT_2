from mypy.config_parser import str_or_array_as_list


class Vacancy():
    """ Класс для вакансий """
    __slots__ = ["id", "name", "employer", "url", "salary_from", "salary_to", "salary_max", "salary_currency", "requirement"]

    def __init__(self, id, name, employer, url, salary, requirement):
        self.id = id
        self.name = name
        self.employer = employer
        self.__validate_salary(salary)
        self.url = url
        self.requirement = requirement

        self.salary_max = max(self.salary_from, self.salary_to)


    def __validate_salary(self, salary: dict):
        """ Приводит зарплату к рабочему формату """

        if salary:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_currency = salary["currency"] if salary["currency"] else None
        else:
            self.salary_from = 0
            self.salary_from = 0
            self.salary_currency = None

        # s_from = salary_from if isinstance(salary_from, (int, float)) else None
        # s_to = salary_to if isinstance(salary_to, (int, float)) else None
        #
        # s_from = max(0, s_from) if s_from is not None else 0
        # s_to = max(0, s_to) if s_to is not None else 0
        #
        # self.salary_from = s_from
        # self.salary_to = s_to
        #
        # self.salary = max(self.salary_from, self.salary_to)
        #
        # self.requirement = requirement or ""


    def __lt__(self, other):
        """ Метод для операции сравнения «меньше» """
        if isinstance(other, Vacancy):
            if self.salary_currency == other.salary_currency:
                return self.salary_max < other.salary_max
            else:
                raise TypeError("Нельзя сравнивать зарплаты с разной валютой")
        else:
            raise TypeError

    def __le__(self, other):
        """ Метод для операции сравнения «меньше или равно» """
        if isinstance(other, Vacancy):
            if self.salary_currency == other.salary_currency:
                return self.salary_max <= other.salary_max
            else:
                raise TypeError("Нельзя сравнивать зарплаты с разной валютой")
        else:
            raise TypeError

    def __gt__(self, other):
        """ Метод для операции сравнения «больше» """
        if isinstance(other, Vacancy):
            if self.salary_currency == other.salary_currency:
                return self.salary_max > other.salary_max
            else:
                raise TypeError("Нельзя сравнивать зарплаты с разной валютой")
        else:
            raise TypeError

    def __ge__(self, other):
        """ Метод для операции сравнения «больше или равно» """
        if isinstance(other, Vacancy):
            if self.salary_currency == other.salary_currency:
                return self.salary_max >= other.salary_max
            else:
                raise TypeError("Нельзя сравнивать зарплаты с разной валютой")
        else:
            raise TypeError


    def __str__(self):
        return (f"Вакансия: {self.name} в компании {self.employer}"
                f"Зарплата {self.salary_from} - {self.salary_from} {self.salary_currency}"
                f"Требования: {self.requirement}"
                f"Ссылка на вакансию: {self.url}")



    # @classmethod
    # def cast_to_object_list(cls, vacancies_json):
    #     vacancies = []
    #     for vacancy in vacancies_json:
    #         obj = cls(id=vacancy.get("id"),
    #                   name=vacancy.get("name"),
    #                   url=vacancy.get("url"),
    #                   salary_from=vacancy.get("salary_from"),
    #                   salary_to=vacancy.get("salary_to"),
    #                   requirement=vacancy.get("requirement"))
    #         vacancies.append(obj)
    #     return vacancies