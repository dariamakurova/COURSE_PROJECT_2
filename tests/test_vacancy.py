
import pytest
from src.vacancy import Vacancy


def test_salary_dict():
    vac = Vacancy("123456", "Dev", "Company Name", "url",
                  {"from": 10000, "to": 20000, "currency": "RUR"}, "requirement")
    assert vac.salary_from == 10000
    assert vac.salary_to == 20000
    assert vac.salary_currency == "RUR"
    assert vac.salary_max == 20000


@pytest.mark.parametrize("currency_input, expected", [
    ("RUB", "RUR"),
    ("РУБ", "RUR"),
    ("РУБ.", "RUR"),
    ("руб.", "RUR"),
])
def test_salary_currency_normalization(currency_input, expected):
    vac = Vacancy("123456", "Dev", "Comp", "url",
                  {"from": 100, "to": 200, "currency": currency_input}, "")
    assert vac.salary_currency == expected


def test_salary_str_full():
    vac = Vacancy("1", "QA", "Test", "url", "100000 - 150000 RUR",
                  "requirement")
    assert vac.salary_from == 100000
    assert vac.salary_to == 150000
    assert vac.salary_currency == "RUR"
    assert vac.salary_max == 150000


def test_salary_str_only_from():
    vac = Vacancy("123456", "QA", "Test", "url", "80000", "requirement")
    assert vac.salary_from == 80000
    assert vac.salary_to == 0
    assert vac.salary_currency is None
    assert vac.salary_max == 80000


def test_salary_none():
    vac = Vacancy("123456", "Dev", "Comp", "url", None, "requirement")
    assert vac.salary_from == 0
    assert vac.salary_to == 0
    assert vac.salary_currency is None
    assert vac.salary_max == 0


def test_comparison_lt():
    v1 = Vacancy("1", "Dev", "C1", "url", {"from": 10, "to": 20, "currency": "RUR"},
                 "")
    v2 = Vacancy("2", "Dev", "C2", "url", {"from": 10, "to": 30, "currency": "RUR"},
                 "")
    assert v1 < v2


def test_comparison_ge():
    v1 = Vacancy("1", "Dev", "C1", "url", {"from": 10, "to": 40, "currency": "RUR"},
                 "")
    v2 = Vacancy("2", "Dev", "C2", "url", {"from": 10, "to": 30, "currency": "RUR"},
                 "")
    assert v1 >= v2


def test_comparison_different_currency():
    v1 = Vacancy("1", "Dev", "C1", "url", {"from": 10, "to": 20, "currency": "RUR"}, "")
    v2 = Vacancy("2", "Dev", "C2", "url", {"from": 10, "to": 20, "currency": "USD"}, "")
    with pytest.raises(TypeError):
        _ = v1 > v2


def test_comparison_invalid_type():
    v1 = Vacancy("1", "Dev", "C1", "url", {"from": 10, "to": 30, "currency": "RUR"}, "")
    with pytest.raises(TypeError):
        _ = v1 > 100


def test_str_method():
    vac = Vacancy("1", "Dev", "Test", "http://example.com",
                  {"from": 100, "to": 200, "currency": "RUR"}, "Уметь")
    text = str(vac)
    assert "Вакансия: Dev" in text
    assert "100 - 200 RUR" in text
    assert "Уметь" in text
    assert "http://example.com" in text
