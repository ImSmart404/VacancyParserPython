import json
class VacancyDTO:
    def __init__(self, title, link, salary, requirement):
        self.title = title
        self.link = link
        self.salary = salary
        self.requirement = requirement

    @staticmethod
    def parse_vacancy_data_hh(data):
        vacancies = []
        for vacancy_info in data:
            title = vacancy_info['name']
            link = vacancy_info['url']
            salary = vacancy_info.get('salary', {}).get('amount', 0)
            requirement = vacancy_info.get('snippet', {}).get('requirement', '')

            vacancy = VacancyDTO(title, link, salary, requirement)
            vacancies.append(vacancy)

        return vacancies

    @staticmethod
    def parse_vacancy_data_sj(data_vacancy) -> list[dict]:
        """
        Организация данных по вакансиям.
        Возвращает сформированный список словарей.
        """
        vacancies = []
        for vacancy in data_vacancy:
            title = vacancy['profession']
            link = vacancy['link']
            salary_from = vacancy.get('payment_from', None)
            salary_to = vacancy.get('payment_to', None)
            requirement = vacancy.get('candidat', None)

            # Устанавливаем значение зарплаты.
            # Если есть обе границы - устанавливаем минимальное значение.
            # В ином случае, устанавливаем то значение, которое существует.
            if salary_from and salary_to:
                salary = min(salary_from, salary_to)
            else:
                salary = salary_from or salary_to

            # Устанавливаем значение требований.
            # Если значение есть - приводим его к нижнему регистру.
            # В ином случае, устанавливаем значение, что данных нет.
            if requirement:
                requirement = requirement.lower()
            else:
                requirement = 'Нет данных.'

            # Проводим проверку, чтобы добавлялись лишь те вакансии, у которых
            # значение зарплаты больше 1000.
            # Добавляем сформированные данные в список.
            if salary > 1000:
                vacancies.append({
                    'title': title,
                    'link': link,
                    'salary': salary,
                    'requirement': requirement
                })

        return vacancies
