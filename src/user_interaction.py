from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies


def user_interaction():

    platforms = ["HeadHunter"]

    search_query = input("Введите поисковый запрос: ")
    vacancies = HeadHunterAPI()
    vacancies_lict = vacancies.get_vacancies(search_query)

    js = JSONSaver()
    js.add_vacancy(vacancies_lict)
    vacs_list = js.get_vacancies()

    while True:
        user_choice = input("Выберите, в каком виде вы хотите получить результаты поиска:\n"
          "1. Вывести все найденные вакансии\n"
          "2. Вывести Топ N вакансий по зарплате\n"
          "3. Вывести вакансии по ключевому слову\n"
          "4. Вывести вакансии в диапозоне зарплат\n").strip()

        available_options = ["1", "2", "3", "4"]
        if user_choice in available_options:
            break
        else:
            print(f"Введите 1, 2, 3 или 4")


    if user_choice == "1":
        print_vacancies(sort_vacancies(vacs_list))

    elif user_choice == "2":
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        print_vacancies(get_top_vacancies(vacs_list, top_n))

    elif user_choice == "3":
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        filtered_vacancies = filter_vacancies(vacs_list, filter_words)
        print_vacancies(filtered_vacancies)

        while True:
            salary_choice = input("Хотите отфильтровать полученные вакансии по зарплате в определенном диапозоне?\n "
                                  "Введите да/нет")

            available_options = ["да", "нет"]
            if salary_choice.lower() in available_options:
                break
            else:
                print(f"Введите да или нет")

        if salary_choice.lower() == "да":
            salary_range = input("Введите диапазон зарплат в формате \"сумма - сумма\": ")
            ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
            print_vacancies(ranged_vacancies)

    elif user_choice == "4":
        salary_range = input("Введите диапазон зарплат в формате \"сумма - сумма\": ")
        ranged_vacancies = get_vacancies_by_salary(vacs_list, salary_range)
        print_vacancies(ranged_vacancies)
