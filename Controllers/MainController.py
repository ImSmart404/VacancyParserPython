from flask import Blueprint, request, json, jsonify, session

from Dto.UserDto import create_user_dto_from_request
from Dto.VacancyDTO import VacancyDTO
from Service.Parser import Parser
from Service.ParseRegionJson import get_city_id
from Service.Users import register_user, login_user

main_controller_app = Blueprint('main_controller', __name__)

main_controller_app.url_prefix = '/main'

data_from_service = None

@main_controller_app.route('/register', methods=['POST'])
def register():
    user_dto = create_user_dto_from_request(request)
    register_user(user_dto.username, user_dto.password)
    return jsonify({'message': 'Registration successful'}), 201


@main_controller_app.route('/login', methods=['POST'])
def login():
    user_dto = create_user_dto_from_request(request)
    if login_user(user_dto.username, user_dto.password):
        session.pop('json_data', None)
        session.pop('service_name', None)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401


@main_controller_app.route('/service', methods=['POST'])
def service():
    global data_from_service
    vacancy_title = request.form.get('vacancy_title')
    global service_name
    service_name = request.form.get('service_name')
    city_name = request.form.get('city_name')
    city_id = get_city_id(service_name, city_name)
    if service_name == "hh":
        data_from_service = Parser.get_vacancies_from_hh(vacancy_title, city_id)
    if service_name == "sj":
        data_from_service = Parser.get_vacancies_from_sj(vacancy_title, city_id)
    # Преобразование данных в формат JSON с использованием json.dumps и добавление параметра default для преобразования обьектов VacancyDTO в словари

    json_data = json.dumps(data_from_service, default=lambda o: o.__dict__, ensure_ascii=False)
    session['json_data'] = json_data
    session['service_name'] = service_name
    return json_data, 200, {'Content-Type': 'application/json; charset=utf-8'}


@main_controller_app.route('/favourites', methods=['POST'])
def favourites():
    link = request.form.get('link')
    json_data = session.get('json_data', '[]')  # Provide a default value as an empty list if 'json_data' is not present
    try:
        # Parse the JSON string to obtain a list of dictionaries
        data_from_service = json.loads(json_data)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON data'}), 400

    # Convert each dictionary to a VacancyDTO object
    vacancies = [VacancyDTO(vacancy['title'], vacancy['link'], vacancy['salary'], vacancy['requirement']) for vacancy in
                 data_from_service]


    target_vacancy = next((vacancy for vacancy in vacancies if vacancy.link == link), None)

    if target_vacancy:
        json_data = json.dumps(target_vacancy.__dict__, ensure_ascii=False)
        return json_data, 200, {'Content-Type': 'application/json; charset=utf-8'}
    else:
        return jsonify({'error': 'Vacancy not found'}), 404
