from flask import Blueprint

app_router = Blueprint('router', __name__)

@app_router.route('/hello')
def hello():
    return 'hello world, this msg from flask backend'