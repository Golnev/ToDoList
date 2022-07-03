from packages.todo import task


class TODOList(task.Task):
    '''class todolist with menu'''

    def __init__(self):
        super().__init__()
        while True:
            # Output operations.
            operation = input('''\n______MENU of TO DO List______
Enter an operation:
1 - Show TO DO List
2 - Add task
3 - Show task by name
4 - Edit task by name
5 - Delete task
6 - Write TO DO List to file
Type "INF" to Help
Type "EXIT" to exit the program\n\n''')
            # Сall methods depending on the selected operation.
            if operation == '1':
                return self.task_list()
            elif operation == '2':
                return self.add_task()
            elif operation == '3':
                return self.find_task()
            elif operation == '4':
                return self.change_task()
            elif operation == '5':
                return self.del_task()
            elif operation == '6':
                file_path = input('Specify the path to write:')
                return self.write_to_file(file_path)
            elif operation == 'INF':
                print(self.cond.__doc__)
            elif operation == 'EXIT':
                self.conn.close()
                break
            else:
                print('\nThis operation does not exist. Enter again.\n')
