from flask import Blueprint, request, json
from Service.Parser import Parser
from Service.ParseRegionJson import get_city_id

main_controller_app = Blueprint('main_controller', __name__)

main_controller_app.url_prefix = '/main'


@main_controller_app.route('/service', methods=['POST'])
def hh():
    vacancy_title = request.form.get('vacancy_title')
    service_name = request.form.get('service_name')
    city_name = request.form.get('city_name')
    city_id = get_city_id(service_name, city_name)
    if (service_name == "hh"):
        data_from_service = Parser.get_vacancies_from_hh(vacancy_title, city_id)
    if (service_name == "sj"):
        data_from_service = Parser.get_vacancies_from_sj(vacancy_title, city_id)
    # Преобразование данных в формат JSON с использованием json.dumps и добавление параметра default для преобразования обьектов VacancyDTO в словари
    json_data = json.dumps(data_from_service, default=lambda o: o.__dict__, ensure_ascii=False)
    return json_data, 200, {'Content-Type': 'application/json; charset=utf-8'}
@main_controller_app.route('/favourites', methods=['POST'])
def favourites():
    vacancy_id = request.form.get('id')

