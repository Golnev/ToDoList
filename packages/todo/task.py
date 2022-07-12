from datetime import datetime
import json
from os import strerror
import packages.todo.exceptions as exceptions
import packages.todo.todolist as todolist
import sqlite3 as s
from sourse import path_to_write
import packages.todo.logger_cl as logger_cl
import packages.todo.JSON_cl as JSON_cl
import json
from packages.crud import request


class Task():
    '''Class for todo application'''
    # A tuple for building a dictionary and validating the input of the day of the week.
    days_week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    to_do_dict = {i: [] for i in days_week}  # Dictionary generator.

    def __init__(self):
        self.conn = s.connect(path_to_write.PATH_TO_SAVE)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Menu class ToDoList.
        """
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        num_of_task INTEGER PRIMARY KEY,
        day_of_week TEXT NOT NULL,
        name_of_task TEXT NOT NULL,
        priority INTEGER NOT NULL,
        datetime_of_create TEXT NOT NULL
        );''')

    def cond(self):
        """This is To Do List.
        Once launched, enter the number of tasks.
        Then you must enter the day of the week, as in: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
        Enter your task number. The number must be between 1 and 15.
        Enter the name of your task. The length of the characters in the task must not be less than 7.
        Enter the priority of the task in the range from 0 to 100.
        The program displays the day of the week (in which there are tasks), the task number, its title, priority
        and the date and time of creation.\n"""

    def create_task(self):
        """Method for creating a task.

        Raises:
            exceptions.PriorityError: Exception if the priority value is invalid.
            exceptions.TaskNameError: Exception if the name of task is invalid.

        Returns:
            tuple: A tuple with the task name, priority, and creation date and time.
        """
        while True:
            try:
                self.priority_task = int(
                    input('Enter priority of task (0 - 100): '))
                if 0 <= self.priority_task <= 100:  # Input validation.
                    break
                else:
                    # Raise exception.
                    raise exceptions.PriorityError(
                        message='\nYour priority out of range 0 - 100.\n')
            except exceptions.PriorityError as e:  # Raise exception for priority.
                logger_cl.priority_log('create_task', self.priority_task)
                print(e.message)
            except ValueError:
                logger_cl.value_error_log('create_task, priority')
                print('\nYou entered a string instead of a number.\n')

        while True:
            try:
                #  Enter name of task.
                self.task_name = input(
                    'Enter name of task (Must be more than 7 letters): ')
                print()
                if len(self.task_name) > 7:  # Input validation.
                    break
                else:
                    # Raise exception.
                    raise exceptions.TaskNameError(
                        message='\nTask name less than 7 letters.\n')
            except exceptions.TaskNameError as e:
                logger_cl.task_name_log('create_task', self.task_name)
                print(e.message)

        # The time and date the task was created, in string form.
        self.date_time = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

        self.task_tuple = (self.task_name, self.priority_task,
                           self.date_time)  # Outputting the result to tuple.
        return self.task_tuple

    def day_of_week(self):
        """_Method for entering the day of the week for the task.

        Raises:
            exceptions.DayOfWeekError: Exception if the day of week is invalid.

        Returns:
            str: Day of week.
        """
        self.days_week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
        while True:
            try:
                self.day = input(
                    'Enter day of week (abbreviated): ').capitalize()  # You can enter day in lowercase.
                if self.day in self.days_week:   # Input validation.
                    return self.day
                else:
                    # Raise exception.
                    raise exceptions.DayOfWeekError(
                        message='\nThe input is invalid. Example: Mon, Tue, Wed, Thu, Fri, Sat, Sun.\n')
            except exceptions.DayOfWeekError as e:
                logger_cl.day_of_week_log('day_of_week', self.day)
                print(e.message)

    def add_task(self):
        """Method for entering tasks.
        """
        while True:
            try:
                amount = int(input('Enter how many tasks you want to enter: '))
                for i in range(amount):
                    # Create tasks.
                    self.to_do_dict[self.day_of_week()] += [self.create_task()]
                    # Сall the function of adding a task to the database.
                    self.add_to_db()
                break
            except ValueError:
                logger_cl.value_error_log('add_task')
                print('\nYou entered a string instead of a number.\n')
        todolist.TODOList()

    def add_to_db(self):
        """Method for adding a task to the database.
        """
        self.c.execute('INSERT INTO tasks (day_of_week, name_of_task, priority, datetime_of_create) VALUES (?, ?, ?, ?)',
                       (self.day, self.task_name, self.priority_task, self.date_time))
        self.conn.commit()
        print('\nTask added successfully!\n')

        self.last_task_in_db()

    def last_task_in_db(self):
        """The method takes the last entered task from the database.
        """
        for row in self.c.execute('SELECT * FROM tasks;'):
            num_task = int(row[0])
            day_week = row[1]
            name_task = str(row[2])
            prior = int(row[3])
            datetime = row[4]

        last_task_dict = {"id": num_task, "day_week": day_week,
                          "name_task": name_task, "prior": prior, "date_time": datetime}

        request.post_task(last_task_dict)

    def task_list_json(self):
        """The method to write to JSON and output a dictionary from JSON.
        """
        ouf_json = open(path_to_write.PATH_JSON, 'w')
        ouf_json.close()
        res = {'ToDolist': []}
        # Assigning values from a database table to variables.
        for row in self.c.execute('SELECT * FROM tasks;'):
            self.num_task = int(row[0])
            self.day_week = row[1]
            self.name_task = str(row[2])
            self.prior = int(row[3])
            self.datetime = row[4]

            # Сreate an object for further writing to a JSON file.
            self.json_obj = JSON_cl.ToDoList(
                self.num_task, self.day_week, self.name_task, self.prior, self.datetime)
            # We encode the object into a dictionary and add it to the end of the list.
            res['ToDolist'].append(JSON_cl.encode(self.json_obj))

            # Decoding JSON into a dictionary.
        #     json_ToDoList_str = json.dumps(
        #         self.json_obj, default=JSON_cl.encode)
        #     ToDoList_dict = json.loads(
        #         json_ToDoList_str, object_hook=JSON_cl.decode)
        #     print(ToDoList_dict.__dict__)

        # print()

        # Write to JSON file.
        ouf_json = open(path_to_write.PATH_JSON, 'a', encoding='utf-8')
        json.dump(res, ouf_json, ensure_ascii=False)
        ouf_json.close()

    def task_list(self):
        """Method for displaying a task match.
        """
        res = ''
        # Assign tasks from a database table to a variable.
        for row in self.c.execute('SELECT * FROM tasks;'):
            res += ('\nTask number: {}\n\tDay of the week: {}\n\tTask name: {}\n\tA priority: {}\n\tDate and time of creation: {}\n'.format(
                row[0], row[1], row[2], row[3], row[4]))
        if res == '':
            print('\nThe task list is empty.\n')
        else:
            # If the database table is not empty, output the result.
            print('\nTask list:\n' + res)
            self.task_list_json()

            # Output ToDOList from JSON:
            print('ToDoList from JSON:')
            request.task_get()

        todolist.TODOList()

    def change_task(self):
        """Method for changing the task.

        Raises:
            exceptions.NumTaskError: Exception if thenumber of task is invalid.
            exceptions.DayOfWeekError: Exception if the day of week is invalid.
            exceptions.PriorityError: Exception if the priority of the task is invalid.
        """
        try:
            # Date and time of change.
            self.date_time_change = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            # The name of the task to search.
            self.num_find_change = int(input('Enter a number of task '))
            # Flag.
            self.find_name = False

            #  Selecting everything from the database table.
            rows = self.c.execute('SELECT * FROM tasks')
            for row in rows:
                if row[0] == self.num_find_change:
                    # Сhange the flag if the task is found and display the result.
                    self.find_name = True
                    print('Task found:\n')
                    print('Task number: {}\n\tDay of the week: {}\n\tTask name: {}\n\tA priority: {}\n\tDate and time of creation: {}\n'.format(
                        row[0], row[1], row[2], row[3], row[4]))
            #  Raise an exception if the task is not found.
            if not self.find_name:
                raise exceptions.NumTaskError(message='\nTask not found.\n')

            # Choose what to change in the task.
            self.what_change = input('''Enter what exactly you want to change in the task:
        1 - Day of the week
        2 - A priority\n''')
            if self.what_change == '1':
                self.day_to_change = input(
                    'Enter day of week (abbreviated): ').capitalize()  # You can enter day in lowercase.
                if self.day_to_change in self.days_week:   # Input validation.
                    # Change the day of the week in a database table.
                    self.c.execute('UPDATE tasks SET day_of_week = ? WHERE num_of_task = ?',
                                   (self.day_to_change, self.num_find_change))
                    # Change the creation date and time.
                    self.c.execute('UPDATE tasks SET datetime_of_create = ? WHERE num_of_task = ?',
                                   (self.date_time_change, self.num_find_change))
                    self.conn.commit()
                    print('\nTask changed\n')
                    request.put_task(self.num_find_change,
                                     self.what_change, self.day_to_change)
                else:
                    # Raise exception.
                    raise exceptions.DayOfWeekError(
                        message='\nThe input is invalid. Example: Mon, Tue, Wed, Thu, Fri, Sat, Sun.\n')

            elif self.what_change == '2':
                self.priority_change = int(
                    input('Enter priority of task (0 - 100): '))
                if 0 <= self.priority_change <= 100:  # Input validation.
                    # Change the priority in the database.
                    self.c.execute('UPDATE tasks SET priority = ? WHERE name_of_task = ?',
                                   (self.priority_change, self.num_find_change))
                    # Change the creation date and time.
                    self.c.execute('UPDATE tasks SET datetime_of_create = ? WHERE name_of_task = ?',
                                   (self.date_time_change, self.num_find_change))
                    self.conn.commit()
                    print('\nTask changed\n')
                    request.put_task(self.num_find_change,
                                     self.what_change, self.priority_change)
                else:
                    # Raise exception.
                    raise exceptions.PriorityError(
                        message='\nYour priority out of range 0 - 100.\n')
            else:
                print('\nEntered invalid operation.')

        # Handle exception and logging.
        except exceptions.NumTaskError as e:
            logger_cl.num__log('change_task')
            print(e.message)
        except exceptions.PriorityError as e:
            logger_cl.priority_log('change_task', self.priority_change)
            print(e.message)
        except exceptions.DayOfWeekError as e:
            logger_cl.day_of_week_log('change_task', self.day_to_change)
            print(e.message)
        except ValueError:
            logger_cl.value_error_log('change_task')
            print('You entered a string instead of a number.\n')
        todolist.TODOList()

    def find_task(self):
        """Method for finding a task.

        Raises:
            exceptions.NumTaskError: Exception if the number of the task is invalid.
        """
        try:
            # The name of the task to search.
            self.task_num = int(input('Enter a number of task: '))
            # Flag.
            self.find_name = False
            #  Selecting everything from the database table.
            rows = self.c.execute('SELECT * FROM tasks')
            for row in rows:
                if row[0] == self.task_num:
                    # Сhange the flag if the task is found and display the result.
                    self.find_name = True
                    print('Task found:\n')
                    print('Task number: {}\n\tDay of week: {}\n\tTask name: {}\n\tA priority: {}\n\tDate and time of creation: {}\n'.format(
                        row[0], row[1], row[2], row[3], row[4]))
            #  Raise an exception if the task is not found.
            if not self.find_name:
                raise exceptions.NumTaskError(message='\nTask not found.\n')
        except exceptions.NumTaskError as e:
            logger_cl.num__log('change_task')
            print(e.message)
        except ValueError:
            logger_cl.value_error_log('change_task')
            print('You entered a string instead of a number.\n')
        finally:
            todolist.TODOList()

    def del_task(self):
        """Method for deleting a task.

        Raises:
            exceptions.DelTaskError: Exception if an error occurred during deletion.
        """
        try:
            # The task number to delete.
            self.num_to_del = int(input('Enter the task number to delete: '))
            # Flag.
            self.find_id = False
            # Selecting everything from a database table.
            rows = self.c.execute('SELECT * FROM tasks')
            for row in rows:
                # If the task is in the table, delete it, if not, raise an exception.
                if row[0] == self.num_to_del:
                    self.find_id = True
            if self.find_id:
                self.c.execute(
                    'DELETE FROM tasks WHERE num_of_task = ?;', (self.num_to_del, ))
                self.conn.commit()
                print('\nRemoval completed successfully\n')
            else:
                raise exceptions.DelTaskError(
                    message='\nThis task number is not in the list.\n')
            request.delete_task(self.num_to_del)
        except exceptions.DelTaskError as e:
            logger_cl.del_task_log(self.num_to_del)
            print(e.message)
        except ValueError:
            logger_cl.value_error_log('del_task, num_to_del')
            print('\nYou entered a string instead of a number.\n')
        todolist.TODOList()

    def write_to_file(self, file_path):
        """Method for writing to a file.

        Args:
            file_path (str): the path of a file to write.
        """
        self.file_path = file_path
        # Select everything from the database table and assign the result to a variable.
        res = ''
        rows = self.c.execute('SELECT * FROM tasks')
        for row in rows:
            res += 'Task number: {}\n\tDay of week: {}\n\tTask name: {}\n\tA priority: {}\n\tDate and time of creation: {}\n'.format(
                row[0], row[1], row[2], row[3], row[4])

        # Write the result to a file.
        try:
            ouf = open(file_path, 'w', encoding='utf-8')
            ouf.write(res)
            ouf.close()

            print('\nWriting to file (path: {}) successfully completed!\n'.format(
                self.file_path))
        except IOError as e:
            logger_cl.IOError_log()
            print('I/O error occurred: ', strerror(e.errno))
        todolist.TODOList()
