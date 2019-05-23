import os
import json


# load config file and return application configs
def load_config():
    # get config file
    CONFIG_FOLDER = os.path.dirname(os.path.abspath(__file__))
    conf_file = os.path.join(CONFIG_FOLDER,
                             'psyched-edge-241413-b32a81efb22b.json')
    # open config file
    with open(conf_file) as config_file:
        config = json.load(config_file)
    return config


def load_os_env():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = \
        'psyched-edge-241413-b32a81efb22b.json'
    return os.environ['GOOGLE_APPLICATION_CREDENTIALS']
