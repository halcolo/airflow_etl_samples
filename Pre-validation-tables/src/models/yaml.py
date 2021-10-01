import yaml
from yaml.loader import SafeLoader, FullLoader

class Yaml():
    def __init__(self, yaml_route):
        self.yaml_route = yaml_route
        with open(self.yaml_route) as f:
            # Decoded is the yaml file translated as python Dict
            self.yaml_decoded = yaml.load(f, Loader=SafeLoader)
    
    def show(self):
        print (yaml.dump(self.yaml_decoded, default_flow_style=False))
        
    def show_decoded(self):
        print(self.yaml_decoded)