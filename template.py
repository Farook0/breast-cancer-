import logging
from pathlib import Path
import os
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

project_name="breast"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "research/trails.ipynb",
    "main.py",
    "templates/index.html",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filenname= os.path.split(file_path)

    if filedir !="":
        os.makedirs(file_path, exist_ok=True)
        logging.info(f"Creating directory {file_path} for file {filenname}")
    if (not os.path.exists(filenname)) or (os.path.getsize(filenname)==0):
        with open(filenname,'w') as f:
            pass
        logging.info(f"Creating empty file {filenname}")