from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies

# тесты для print_vacancies:


def test_print_vacancies(capsys, vacancies_list):
    print_vacancies(vacancies_list)
    outer = capsys.readouterr().out
    assert "Разработчик" in outer
    assert "Тестировщик" in outer
    assert "Аналитик" in outer


# тесты для filter_vacancies


def test_filter_vacancies_keyword(vacancies_list):
    result = filter_vacancies(vacancies_list, ["Python"])
    assert len(result) == 2
    assert all("python" in (r.requirement.lower() + r.name.lower()) for r in result)


def test_filter_vacancies_no_keywords(vacancies_list):
    result = filter_vacancies(vacancies_list, [])
    assert result == vacancies_list


def test_filter_vacancies_keyword_not_found(vacancies_list):
    result = filter_vacancies(vacancies_list, ["Что-то"])
    assert len(result) == 0


# тесты для get_vacancies_by_salary


def test_get_vacancies_salary_range_valid(vacancies_list):
    result = get_vacancies_by_salary(vacancies_list, "120000 - 160000")
    assert len(result) == 2
    assert all(120000 <= vac.salary_max <= 160000 for vac in result)


def test_get_vacancies_salary_range_only_from(vacancies_list):
    result = get_vacancies_by_salary(vacancies_list, "160000 -")
    assert len(result) == 1
    assert result[0].name == "Аналитик"


def test_get_vacancies_salary_range_invalid_format(vacancies_list, capsys):
    result = get_vacancies_by_salary(vacancies_list, "от 100000")
    outer = capsys.readouterr().out
    assert "Некорректный ввод" in outer
    assert result == vacancies_list


def test_get_vacancies_salary_empty(vacancies_list):
    result = get_vacancies_by_salary(vacancies_list, "")
    assert result == vacancies_list


# тесты для sort_vacancies


def test_sort_vacancies(vacancies_list):
    result = sort_vacancies(vacancies_list)
    assert result[0].salary_max >= result[1].salary_max >= result[2].salary_max


# тесты для get_top_vacancies


def test_get_top_vacancies_default(vacancies_list):
    result = get_top_vacancies(vacancies_list, 2)
    assert len(result) == 2
    assert "Разработчик", "Аналитик" in result
    assert "Тестировщик" not in result
