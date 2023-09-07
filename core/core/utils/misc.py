import yaml


def yaml_coerce(value):
    # Convert string value to proper Python dict
    # E.g., converts string "{'apples':1,'bacon':2}" to Python dict
    # Useful in stringify settings such as Dockerfile
    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
