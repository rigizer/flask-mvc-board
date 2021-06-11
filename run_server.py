import pymysql          # pip3 install pymysql

from flask import Flask, render_template, request, redirect     # pip3 install flask

from controller.index_controller import index_controller

db_config = {
    'user': 'py_user', 
    'password': 'py_5869', 
    'host': 'localhost', 
    'database': 'py_web', 
    'port': 3306, 
    'charset': 'utf-8'
}

def run():
    # conn = pymysql.connect(**config)
    app = Flask(__name__)

    app.register_blueprint(index_controller)
    
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    run()