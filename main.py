from packages.todo import todolist, logger_cl
import configparser
from docs import path


config = configparser.ConfigParser()
config.read(path.PATH_CONFIG)


print('Hello {}!'.format(config['db']['user']))
while True:
    password = input('Enter password to start programm or EXIT to close programm: ')
    if password == config['db']['password']:
        obj = todolist.TODOList()
        break
    elif password == 'EXIT':
        break
    else:
        logger_cl.password_log()
        print('Wrong password!')
