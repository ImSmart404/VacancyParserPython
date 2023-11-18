from flask import Blueprint, render_template, request, jsonify, json
from Service.HhParser import HeadHunterParser

main_controller_app = Blueprint('main_controller', __name__)

main_controller_app.url_prefix = '/main'


@main_controller_app.route('/', methods=['POST'])
def index():
    vacancy_title = request.form.get('vacancy_title')
    data_from_hh = HeadHunterParser.get_vacancies(vacancy_title, 1)

    # Преобразование данных в формат JSON с использованием json.dumps и добавление параметра default для преобразования обьектов VacancyDTO в словари
    json_data = json.dumps(data_from_hh, default=lambda o: o.__dict__, ensure_ascii=False)
    return json_data, 200, {'Content-Type': 'application/json; charset=utf-8'}
