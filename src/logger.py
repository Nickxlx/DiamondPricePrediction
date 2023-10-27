import logging
# interact with the os including creating directories and working with file paths.
import os
from datetime import datetime

# defining struct of logger folder 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# creating path use to join(create) current working dir with LOG_FILE folder inside the logs folder
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# creating a new file using path
os.makedirs(logs_path, exist_ok=True)

# ues to join(create) LOG_FILE folder inside the logs_path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
