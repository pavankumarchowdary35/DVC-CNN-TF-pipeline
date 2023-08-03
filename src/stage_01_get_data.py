import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories, copy_files
import random


STAGE = "STAGE_NAME" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def get_data(config_path: str) -> None:
    ## read config files
    config = read_yaml(config_path)

    source_data_dirs = config["source_data_dirs"]
    local_data_dirs = config["local_data_dirs"]

    N = len(source_data_dirs)
    for source_data_dir, local_data_dir in zip(source_data_dirs,local_data_dirs):
        create_directories([local_data_dir])
        copy_files(source_data_dir, local_data_dir)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage one started <<<<<")
        get_data(config_path=parsed_args.config)
        logging.info(f">>>>> stage one completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e