import yaml
import os

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.yaml')
    return load_yaml(config_path)

def get_users():
    users_path = os.path.join(os.path.dirname(__file__), '../data/users.yaml')
    return load_yaml(users_path)