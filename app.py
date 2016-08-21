from os import path, walk

from flask import Flask

from blueprints import blueprints


def create_app(environment=None):
    app = Flask(__name__)

    # Configuration -----------------------------------------------------------
    cwd = path.dirname(path.abspath(__file__))
    config_dir = path.join(cwd, 'config')

    config_files = []
    for (root, dir_names, file_names) in walk(config_dir):
        for file_name in file_names:
            config_files.append(path.join(root, file_name))
    config_files = sorted(config_files)

    for config_file in config_files:
        app.config.from_pyfile(config_file)

        if environment:
            if environment in config_file:
                break # only go as deep as the runtime

    # Blueprints --------------------------------------------------------------
    app.register_blueprint(blueprints)

    return app
