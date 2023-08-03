import os
import yaml
import logging
import time
import pandas as pd
import json
import shutil
import tqdm

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")

def copy_files(source_dir: str,local_dir: str) -> None:
    list_of_files = os.listdir(source_dir)
    N = len(list_of_files)

    for filename in list_of_files:
        src = os.path.join(source_dir,filename)
        dest = os.path.join(local_dir,filename)
        shutil.copy(src,dest)

    logging.info(
        f"all the files has been copied from {source_dir} to {local_dir}"  
    )

def get_timestamp(name: str) -> str:
    """create unique name with timestamp

    Args:
        name (str): name of file or directory

    Returns:
        str: unique name with timestamp
    """
    timestamp = time.asctime().replace(" ", "_").replace(":", ".")
    unique_name = f"{name}_at_{timestamp}"
    return unique_name
    




    






def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")