from src.models.yaml import Yaml

if __name__ == '__main__':

    yaml = Yaml('sample.yml')
    
    yaml.show()
    yaml.show_decoded()