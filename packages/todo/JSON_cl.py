class ToDoList:
    """Class to write to JSON"""

    def __init__(self, id, day_week, name_task, prior, date_time):
        self.id = id
        self.day_week = day_week
        self.name_task = name_task
        self.prior = prior
        self.date_time = date_time


def encode(w):
    """Encoding function for writing to json.

    Args:
        w (class): Accepts the class ToDoList.

    Raises:
        TypeError: Raise an error if the class is not ToDoList.

    Returns:
        dict : Return the dictionary of the class.
    """
    if isinstance(w, ToDoList):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializanle')


def decode(w):
    """JSON decode function.

    Args:
        w (class): Accepts the class ToDoList.

    Returns:
        class: ToDoList class.
    """
    return ToDoList(w['num_task'], w['day_week'], w['name_task'], w['prior'], w['date_time'])
