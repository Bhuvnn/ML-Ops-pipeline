import yaml
def load_params(path):
    with open(path,"r") as f:
        params=yaml.safe_load(f)
    return params

params=load_params("params.yaml")
value=params["data_ingestion"]
print(type(value))