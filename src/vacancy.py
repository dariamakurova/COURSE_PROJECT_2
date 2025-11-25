from mypy.config_parser import str_or_array_as_list


class Vacancy():
    """ Класс для вакансий """

    def __init__(self, name, url, salary_from=None, salary_to=None, requirement=""):
        self.name = self._validate_name(name)
        self.url = self._validate_url(url)
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement

    @staticmethod
    def _validate_name(name):
        if not name or not isinstance(name, str):
            return "Без названия"
        return name.strip()

    @staticmethod
    def _validate_url(url):
        if not url or not isinstance(url, str) or not url.startswith("http"):
            return "Ссылка не указана"
        return url.strip()

    def _validate_salary(self, salary_from, salary_to):

        if isinstance(salary_from, dict) and salary_to is None:
            salary_to = salary_from.get('to')
            salary_from = salary_from.get('from')

        s_from = salary_from if isinstance(salary_from, (int, float)) else None
        s_to = salary_to if isinstance(salary_to, (int, float)) else None

        s_from = max(0, s_from) if s_from is not None else 0
        s_to = max(0, s_to) if s_to is not None else 0

        return s_from, s_to
