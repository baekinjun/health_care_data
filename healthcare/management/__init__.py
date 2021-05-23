def create_app():
    from flask import Flask
    from flask_cors import CORS
    from apps.middleware import swagger
    app = Flask(__name__)
    CORS(app)
    app.config['SWAGGER'] = {
        'title': 'health care data',
        'uiversion': 2
    }
    swagger.init_app(app)

    from apps import statics_api, search_api
    app.register_blueprint(statics_api)
    app.register_blueprint(search_api)

    return app
