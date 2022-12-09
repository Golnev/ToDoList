from os import path

# To write a database to a folder sourse.
ROOT_DIR = path.dirname(path.abspath(__file__))
FILE_TO_SAVE = 'MyToDoList.db'
PATH_TO_SAVE = path.join(ROOT_DIR, FILE_TO_SAVE)  # Path to write txt file.


JSON_FILE = 'result.json'
PATH_JSON = path.join(ROOT_DIR, JSON_FILE)  # Path to write JSON.
