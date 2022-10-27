import yaml 

def yaml_print(tables):
    document = """
    >> print(yaml.dump(yaml.load(document), default_flow_style=False))