import json
import os

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def test_json_saver_new_file():
    test_file = "test_vacancies.json"
    saver = JSONSaver(path=test_file)

    assert os.path.exists(saver._JSONSaver__filename)
    with open(saver._JSONSaver__filename, "r", encoding="utf-8") as file:
        assert json.load(file) == []


def test_add_dict_vacancy(vacancy_dict):
    test_file = "test_vacancies.json"
    saver = JSONSaver(test_file)
    saver.delete_vacancy()

    saver.add_vacancy(vacancy_dict)

    with open(saver._JSONSaver__filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 1
    assert data[0]["vac_id"] == "93353083"


def test_add_object_vacancy(vacancy_obj):
    test_file = "test_vacancies.json"
    saver = JSONSaver(test_file)
    saver.delete_vacancy()

    saver.add_vacancy(vacancy_obj)

    with open(saver._JSONSaver__filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["vac_id"] == "123456"
    assert data[0]["salary"]["currency"] == "RUR"


def test_prevent_duplicate(vacancy_obj):
    test_file = "test_vacancies.json"
    saver = JSONSaver(test_file)
    saver.delete_vacancy()

    saver.add_vacancy(vacancy_obj)
    saver.add_vacancy(vacancy_obj)

    with open(saver._JSONSaver__filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 1  # duplicate prevented


def test_get_vacancies(vacancy_obj):
    test_file = "test_vacancies.json"
    saver = JSONSaver(test_file)
    saver.delete_vacancy()
    saver.add_vacancy(vacancy_obj)

    vacancies = saver.get_vacancies()

    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].vac_id == "123456"


def test_delete_vacancy_success(vacancy_obj):
    test_file = "test_vacancies.json"
    saver = JSONSaver(test_file)
    saver.delete_vacancy()
    saver.add_vacancy(vacancy_obj)

    result = saver.delete_vacancy(vacancy_obj)

    assert result is True

    with open(saver._JSONSaver__filename, "r", encoding="utf-8") as file:
        assert json.load(file) == []


def test_delete_vacancy_not_found(vacancy_obj, capsys):
    test_file = "test_vacancies.json"
    saver = JSONSaver(test_file)
    saver.delete_vacancy()
    saver.add_vacancy(vacancy_obj)

    vac_del = Vacancy(vac_id="654321", name="", employer="", url="", salary={}, requirement="")
    result = saver.delete_vacancy(vac_del)

    outer = capsys.readouterr()

    assert result is False
    assert "не найдена" in outer.out


def test_delete_all():
    test_file = "test_vacancies.json"
    saver = JSONSaver(test_file)

    saver.add_vacancy({"vac_id": "1"})
    saver.add_vacancy({"vac_id": "2"})

    result = saver.delete_vacancy()

    assert result is True

    with open(saver._JSONSaver__filename, "r", encoding="utf-8") as file:
        assert json.load(file) == []
