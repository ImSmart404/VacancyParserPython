from flask import Blueprint, render_template, request, jsonify, json
from Service.HhParser import HeadHunterParser
from Service.SuperJopParser import SuperJobParser
from Service.ParseRegionJson import get_city_id

main_controller_app = Blueprint('main_controller', __name__)

main_controller_app.url_prefix = '/main'


@main_controller_app.route('/hh', methods=['POST'])
def hh():
    vacancy_title = request.form.get('vacancy_title')
    service_name = request.form.get('service_name')
    city_name = request.form.get('city_name')
    city_id = get_city_id(service_name, city_name)
    data_from_hh = HeadHunterParser.get_vacancies(vacancy_title, city_id)
    # Преобразование данных в формат JSON с использованием json.dumps и добавление параметра default для преобразования обьектов VacancyDTO в словари
    json_data = json.dumps(data_from_hh, default=lambda o: o.__dict__, ensure_ascii=False)
    return json_data, 200, {'Content-Type': 'application/json; charset=utf-8'}


@main_controller_app.route('/sj', methods=['POST'])
def sj():
    vacancy_title = request.form.get('vacancy_title')
    service_name = request.form.get('service_name')
    city_name = request.form.get('city_name')
    city_id = get_city_id(service_name, city_name)
    data_from_sj = SuperJobParser.get_vacancies(vacancy_title, city_id)
    # Преобразование данных в формат JSON с использованием json.dumps и добавление параметра default для преобразования обьектов VacancyDTO в словари
    json_data = json.dumps(data_from_sj, default=lambda o: o.__dict__, ensure_ascii=False)
    return json_data, 200, {'Content-Type': 'application/json; charset=utf-8'}
