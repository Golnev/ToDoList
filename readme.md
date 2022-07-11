# ToDoList

[![Code style: autopep8](https://img.shields.io/badge/code%20style-autopep8-yellow)](https://github.com/hhatto/autopep8)

- [Описание программы](#описание-программы)
- [Запись данных](#запись-данных)
  - [SQLite](#SQLite)
  - [JSON](#JSON)
- [Запуск сервера](#запуск-сервера)
- [Запуск программы](#запуск-программы)
  - [Первый запуск](#первый-запуск)
- [Меню ToDoList](#меню-ToDoList)
  - [Show ToDoList](#Show-ToDoList)
  - [Add task](#Add-task)
  - [Show task by number](#Show-task-by-number)
  - [Edit task by number](#Edit-task-by-number)
  - [Delete task](#Delete-task)
  - [Write TO DO List to file](#Write-TO-DO-List-to-file)
  - [INF](#INF)
  - [EXIT](#EXIT)
- [Logger](#logger)

## Описание программы

Программа ToDoList предназначена для записи ваших задач и дел.
У каждой задачи есть номер (присваивается автоматически, по порядку), имя (что необходимо сделать), день недели (когда планируете сделать), приоритет, дата и время создания.

ToDoList имеет возможность добавить нескольких задач, отражать список задач, показывать определенную задачу, редактировать определенную задачу, удалять задачу и записывать список задач в txt файл.

## Запись данных

Список задач храниться в базе данных SQLite и на JSON-server.

### SQLite

База данных SQLite создается автоматически.
Путь к базе данных: \sourse\MyToDoList.db

### JSON

Путь к JSON: \sourse\ToDoList.json

Пример ToDoList.json:

```
{
    "ToDolist": []
}
```

Дополнительно список задач записывается в отдельный JSON файл.
Путь к нему: \sourse\result.json

## Запуск сервера

Для запуска сервера необходимо ввести:

```
json-server --watch ToDoList.json
```

Путь к ToDoList.json: \sourse\ToDoList.json

После ввода измените host в \docs\config.ini на Ваш.

```
[DEFAULT]
host = http://localhost:3000/ToDolist
```

## Запуск программы

Для запуска программы запустите файл main.py.

main.py находится в корневой папке.

Программа приветствует Вас и просит ввести пароль.
Пароль не отображается при вводе.

Пример:

```
Hello UserName!
Enter password to start programm or EXIT to close programm:
```

### Первый запуск

При первом запуске программы измените имя пользователя и установите пароль для входа в программу в файле config.ini.

Путь к config.ini: \docs\config.ini

Пример:

```
[db]
user = UserName
password = password
```

## Меню ToDoList

После ввода пароля отображается меню ToDoList.
Меню показывает все возможные операции и просит выбрать одну из них.

```
______MENU of TO DO List______
Enter an operation:
1 - Show TO DO List
2 - Add task
3 - Show task by number
4 - Edit task by number
5 - Delete task
6 - Write TO DO List to file
Type "INF" to Help
Type "EXIT" to exit the program
```

### Show ToDoList

Отображает список Ваших задач из базы данных и json-сервера.

Вызывается вводом "1".

```
1

Task list:

Task number: 1
        Day of the week: Mon
        Task name: TEST TEST TEST
        A priority: 10
        Date and time of creation: 11/07/2022, 20:27:16

ToDoList from JSON:

Task number: 1
            Day of the week: Mon
            Task name: TEST TEST TEST
            A priority: 10
            Date and time of creation: 11/07/2022, 20:27:16
```

Если задачи в списке нет - пишет, что список задач пуст.

```
1

The task list is empty.
```

### Add task

Добавляет задачу(задачи) в ToDoList.

Вызывается вводом "2".

Необходимо указать количество задач, которое хотите внести, день недели (сокращенно), приоритет (от 0 до 100), название задачи (больше 7 символов).

```
2
Enter how many tasks you want to enter: 1
Enter day of week (abbreviated): mon
Enter priority of task (0 - 100): 10
Enter name of task (Must be more than 7 letters): TEST TEST TEST
```

После выводится сообщение, что задача добавлена успешно в базу данных и json-сервер.

```
Task added successfully!

Task in JASON added successfully!
```

### Show task by number

Отображает задачу по введенному номеру.
Вызывается вводом "3".

```
3
Enter a number of task: 1
Task found:

Task number: 1
        Day of week: Mon
        Task name: TEST TEST TEST
        A priority: 10
        Date and time of creation: 11/07/2022, 20:54:21
```

Если задачи с таким номером нет, выводится сообщение, что данная задача не найдена.

```
3
Enter a number of task: 2

Task not found.
```

### Edit task by number

Редактирует задачу по введенному номеру.

Вызывается вводом "4".

Возможно отредактировать либо день недели (вводом "1"), либо приоритет (вводом "2").

```
4
Enter a number of task 1
Task found:

Task number: 1
        Day of the week: Mon
        Task name: TEST TEST TEST
        A priority: 10
        Date and time of creation: 11/07/2022, 20:57:02

Enter what exactly you want to change in the task:
        1 - Day of the week
        2 - A priority
1
Enter day of week (abbreviated): fri

Task changed

Task in JASON changed successfully!
```

### Delete task

Удаляет задачу.

Вызывается вводом "5".

Необходмо указать номер удаляемой задачи.

### Write TO DO List to file

Записывает список задач в txt файл.

Вызывается вводом "6".

При записи указать путь, где необходимо создать файл, с расширением .txt.

```
6
Specify the path to write:путь\ToDolist.txt

Writing to file (path: путь\ToDolist.txt) successfully completed!
```

### INF

Выводит информацию о программе.

Вызывается вводом "INF".

```
INF
This is To Do List.
        Once launched, enter the number of tasks.
        Then you must enter the day of the week, as in: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
        Enter your task number. The number must be between 1 and 15.
        Enter the name of your task. The length of the characters in the task must not be less than 7.
        Enter the priority of the task in the range from 0 to 100.
        The program displays the day of the week (in which there are tasks), the task number, its title, priority
        and the date and time of creation.
```

### EXIT

Выход из программы.

Вызывается вводом "EXIT".

## Logger

Путь к logger: \docs\logger_file.log

- **Source code:** https://github.com/Golnev/ToDoList
