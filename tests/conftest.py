import pytest


@pytest.fixture
def vacancy_data_hh():
    return {"id":"93353083","premium":False,"name":"Тестировщик",
                      "department": None,"has_test":False,"response_letter_required":False,
                      "area":{"id":"26","name":"Воронеж","url":"https://api.hh.ru/areas/26"},
                      "salary":{"from":350000,"to":450000,"currency":"RUR","gross":False},
                      "type":{"id":"open","name":"Открытая"},"address":None,"response_url":None,
                      "sort_point_distance":None,"published_at":"2024-02-16T14:58:28+0300",
                      "created_at":"2024-02-16T14:58:28+0300","archived":False,
                      "apply_alternate_url":"https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
                      "branding":{"type":"CONSTRUCTOR","tariff":"BASIC"},"show_logo_in_search":True,
                      "insider_interview":None,
                      "url":"https://api.hh.ru/vacancies/93353083?host=hh.ru",
                      "alternate_url":"http://example.com","relations":[],
                      "employer":{"id":"3499705","name":"Company",
                                  "url":"https://api.hh.ru/employers/3499705"},
                      "snippet":{"requirement":"Тестовые требования",
                                 "responsibility":"Оценивать вид из окна: встречать рассветы на кухне, "
                                                  "и провожать алые закаты в спальне. Оценивать инфраструктуру района"}}

@pytest.fixture
def vacancy_data_json():
    return {"items": [{"id":"123456","premium":False,"name":"Тестировщик",
                      "salary":{"from":350000,"to":450000,"currency":"RUR","gross":False},
                      "url":"https://api.hh.ru/vacancies/1234563?host=hh.ru",
                      "alternate_url":"http://example.com",
                      "employer":{"id":"3499705","name":"Company",
                                  "url":"https://api.hh.ru/employers/1"},
                      "snippet":{"requirement":"Тестовые требования",
                                 "responsibility":"Тестовые обязанности"}},
                       {"id": "123457", "premium": False, "name": "Программист",
                        "salary": {"from": 350000, "to": 450000, "currency": "USD", "gross": False},
                        "url": "https://api.hh.ru/vacancies/123457?host=hh.ru",
                        "alternate_url": "http://example.com",
                        "employer": {"id": "3499705", "name": "Other Company",
                                     "url": "https://api.hh.ru/employers/2"},
                        "snippet": {"requirement": "Тестовые требования",
                                    "responsibility": "Тестовые обязанности"}}
                       ]}