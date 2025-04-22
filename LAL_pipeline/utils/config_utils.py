import yaml

def load_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
def save_config(config, config_path):
    with open(config_path, "w") as f:
        yaml.safe_dump(config, f, default_flow_style=False, sort_keys=False)    