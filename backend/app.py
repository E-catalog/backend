import logging

from flask import Flask
from werkzeug.exceptions import BadRequest, InternalServerError, MethodNotAllowed, NotFound

from backend.views import Individuals, places

logger = logging.getLogger(__name__)


def handle_bad_request(error: BadRequest):
    return {'error': 'Bad request'}, 400


def handle_not_found(error: NotFound):
    return {'error': 'Not found'}, 404


def handle_method_not_allowed(error: MethodNotAllowed):
    return {'error': 'Method not allowed'}, 405


def handle_internal_server_error(error: InternalServerError):
    return {'error': 'Internal server error'}, 500


def create_app():
    app = Flask(__name__)

    app.register_blueprint(Individuals.routes, url_prefix='/api/v1/individuals/')
    app.register_blueprint(places.routes, url_prefix='/api/v1/places/')

    app.register_error_handler(BadRequest, handle_bad_request)
    app.register_error_handler(NotFound, handle_not_found)
    app.register_error_handler(MethodNotAllowed, handle_method_not_allowed)
    app.register_error_handler(InternalServerError, handle_internal_server_error)

    return app


app = create_app()
