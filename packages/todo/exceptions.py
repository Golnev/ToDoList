class TaskTroubles(Exception):
    '''Main class for exceptions.'''

    def __init__(self, head='HeadError', message=''):
        super().__init__()
        self.head = head
        self.message = message


class PriorityError(TaskTroubles):
    '''Class for exceptions when working with task priority.'''

    def __init__(self, head='PriorError', message='Bad priority!'):
        super().__init__()
        self.head = head
        self.message = message


class TaskNameError(TaskTroubles):
    '''Class for exceptions when working with task names.'''

    def __init__(self, head='TaskNError', message='Bad Name'):
        super().__init__()
        self.head = head
        self.message = message


class DayOfWeekError(TaskTroubles):
    '''Class for exceptions when working with days of the week.'''

    def __init__(self, head='DayOfWError', message= 'Bad day'):
        super().__init__()
        self.head = head
        self.message = message


class DelTaskError(TaskTroubles):
    '''Class for exceptions when deleting a task.'''

    def __init__(self, head='DelTaskError', message='Bad task!'):
        super().__init__()
        self.message = message
        self.head = head
