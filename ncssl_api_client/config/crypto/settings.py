import yaml
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "/settings.yaml", 'r') as f:
    settings = yaml.load(f)

locals().update(settings)