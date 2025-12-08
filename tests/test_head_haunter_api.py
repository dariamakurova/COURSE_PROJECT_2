from unittest.mock import patch

from src.head_hunter_api import HeadHunterAPI


def test_simplify_vacancy(vacancy_data_hh):

    result = HeadHunterAPI.simplify_vacancy(vacancy_data_hh)

    assert result["vac_id"] == "93353083"
    assert result["name"] == "Тестировщик"
    assert result["employer"] == "Company"
    assert result["url"] == "http://example.com"
    assert result["salary"]["currency"] == "RUR"
    assert result["requirement"] == "Тестовые требования"


def test_get_vacancies(vacancy_data_json):
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = vacancy_data_json

        mock_get.retuen_value.raise_for_status.return_value = None
        api = HeadHunterAPI()
        api._HeadHunterAPI__params["page"] = 19
        vacancies = api.get_vacancies("python")

    assert len(vacancies) == 1
    assert vacancies[0]["vac_id"] == "123456"
    assert vacancies[0]["employer"] == "Company"

    assert mock_get.call_count == 1
