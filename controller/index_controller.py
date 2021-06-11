from flask import Flask, render_template, request, redirect, Blueprint     # pip3 install flask

index_controller = Blueprint('index_controller', __name__)

@index_controller.route('/', methods=['GET'])
@index_controller.route('/index', methods=['GET'])
def index():
    return render_template('index.htm')