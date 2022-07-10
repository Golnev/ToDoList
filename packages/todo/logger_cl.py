import logging
from docs import path as path_to_write


FORMAT = '%(levelname)s:%(asctime)s - %(message)s'  # File Write Format.

logging.basicConfig(level=logging.WARNING,
                    filename=path_to_write.PATH_LOGGER, filemode='a', format=FORMAT)

logger = logging.getLogger()


def value_error_log(def_name: str) -> str:
    """Function for logging, if not an integer was entered.

    Args:
        def_name (str): The name of the function to write from.

    Returns:
        str: Description of the problem.
    """
    logger.critical('Method: {} - ValueError: str, need int.'.format(def_name))


def num__log(def_name: str) -> str:
    """Function for logging, if invalid number of task was entered.

    Args:
        def_name (str): The name of the function to write from.

    Returns:
        str: Description of the problem.
    """
    logger.warning('Method: {} - inalid number of task'.format(def_name))


def priority_log(def_name: str, num: int) -> str:
    """Function for logging if the wrong priority was entered.

    Args:
        def_name (str): The name of the function to write from.
        num (int): The priority number that entered.

    Returns:
        str: Description of the problem.
    """
    logger.warning(
        'Method: {}, Entered priority: {} - out of range.'.format(def_name, num))


def task_name_log(def_name: str, task_name: str) -> str:
    """Function for logging if the wrong task name was entered.

    Args:
        def_name (str): The name of the function to write from.
        task_name (str): The name of the task that entered.

    Returns:
        str: Description of the problem.
    """
    logger.warning(
        'Method: {}, Entered task name: {} - invalid task name.'.format(def_name, task_name))


def del_task_log(num_task: int) -> str:
    """Function for logging if the wrong number of task was entered.

    Args:
        num_task (int): The name of the function to write from.

    Returns:
        str: Description of the problem.
    """
    logger.warning(
        'Method: del_task, Entered num of task {} - invalid num of task'.format(num_task))


def IOError_log() -> str:
    """Function for logging if an error occurred while writing to a file.

    Returns:
        str: Description of the problem.
    """
    logger.critical('Error writing to file.')


def day_of_week_log(def_name: str, day_of_week: str) -> str:
    """Function for loggin if the wrong day of week was entered.

    Args:
        def_name (str): The name of the function to write from.
        day_of_week (str): _description_

    Returns:
        str: Description of the problem.
    """
    logger.warning(
        'Method: {}, Entered day of week {} - invalid day of week.'.format(def_name, day_of_week))


def password_log() -> str:
    """Function for logging if the wrong password was entered.

    Returns:
        str: Description of the problem.
    """
    logger.critical('Invalid password!')
