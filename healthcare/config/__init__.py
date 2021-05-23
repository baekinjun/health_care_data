import yaml

with open('config/config.yaml') as f:
    settings = yaml.load(f, Loader=yaml.Loader)

Database_config = settings['DATABASE']