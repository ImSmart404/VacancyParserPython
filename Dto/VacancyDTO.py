import json
class VacancyDTO:
    def __init__(self, title, link, salary, requirement):
        self.title = title
        self.link = link
        self.salary = salary
        self.requirement = requirement


    @staticmethod
    def parse_vacancy_data(data):
        vacancies = []
        for vacancy_info in data:
            title = vacancy_info['name']
            link = vacancy_info['url']
            salary = vacancy_info.get('salary', {}).get('amount', 0)
            requirement = vacancy_info.get('snippet', {}).get('requirement', '')

            vacancy = VacancyDTO(title, link, salary, requirement)
            vacancies.append(vacancy)

        return vacancies
