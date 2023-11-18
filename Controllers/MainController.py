from flask import Blueprint, render_template, request
from Service.HhParser import HhParser

main_controller_app = Blueprint('main_controller', __name__)

main_controller_app.url_prefix = '/main'


@main_controller_app.route('/', methods=['POST'])
def index():
    vacancy_title = request.form.get('vacancy_title')
    data_from_hh = HhParser.get_data(vacancy_title)
    return f"Данные для вакансии '{vacancy_title}' из HH.ru: {data_from_hh}"