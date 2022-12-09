from packages.todo import todolist
import configparser
from docs import path


config = configparser.ConfigParser()
config.read(path.PATH_CONFIG)

obj = todolist.TODOList()
