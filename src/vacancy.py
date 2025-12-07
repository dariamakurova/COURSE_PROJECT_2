from mypy.config_parser import str_or_array_as_list


class Vacancy():
    """ Класс для вакансий """
    __slots__ = ["vac_id", "name", "employer", "url", "salary_from", "salary_to", "salary_max", "salary_currency", "requirement"]

    def __init__(self, vac_id, name, employer, url, salary, requirement):
        self.vac_id = vac_id
        self.name = name
        self.employer = employer
        self.__validate_salary(salary)
        self.url = url
        self.requirement = requirement

        self.salary_max = max(self.salary_from, self.salary_to)


    def __validate_salary(self, salary: dict):
        """ Приводит зарплату к рабочему формату """

        rur_currencies = {"RUR" : "RUR",
                          "RUB": "RUR",
                          "РУБ": "RUR",
                          "РУБ.": "RUR"}

        if salary:
            if isinstance(salary, dict):
                self.salary_from = salary["from"] if salary.get("from") else 0
                self.salary_to = salary["to"] if salary.get("to") else 0
                self.salary_currency = salary["currency"] if salary.get("currency") else None

            elif isinstance(salary, str):

                self.salary_from = 0
                self.salary_to = 0
                self.salary_currency = None

                salary_details = salary.split("-")
                if len(salary_details) >= 1 and salary_details[0].strip().isdigit():
                    self.salary_from = int(salary_details[0])

                if len(salary_details) >= 2 and salary_details[1].split()[0].strip().isdigit():
                    self.salary_to = int(salary_details[1].split()[0].strip())

                    if len(salary_details[1].split()) >= 2:
                        currency = salary_details[1].split()[1].strip().upper()
                        self.salary_currency = rur_currencies.get(currency, currency)
        else:
            self.salary_from = 0
            self.salary_to = 0
            self.salary_currency = None


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
        return (f"Вакансия: {self.name} в компании {self.employer}\n"
                f"Зарплата {self.salary_from} - {self.salary_to} {self.salary_currency}\n"
                f"Требования: {self.requirement}\n"
                f"Ссылка на вакансию: {self.url}\n")
