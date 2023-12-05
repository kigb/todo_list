from datetime import datetime
class TodoListItem:
    """
    A class to represent a todo_list item with status.

    Attributes:
        task_name (str): Name or description of the task.
        task_id (int): Unique identifier for the task.
        status (str): Status of the task ('未完成', '已完成', '已过期').
    """
    _id_counter = 0  # Class variable to keep track of the last assigned ID

    def __init__(self, task_name, due_date):
        """
        Constructor for TodoListItem.

        Args:
            task_name (str): Name or description of the task.
            due_date (datetime): Due date of the task.
        """
        self.task_name = task_name
        self.task_id = TodoListItem._get_next_id()
        self.due_date = due_date

        # Convert both datetime objects to date objects for comparison
        today_date = datetime.today().date()
        due_date_date = due_date.date()

        self.status = '未完成' if today_date <= due_date_date else '已过期'

    @classmethod
    def _get_next_id(cls):
        """
        Class method to get the next unique ID for a task.

        Returns:
            int: The next unique task ID.
        """
        cls._id_counter += 1
        return cls._id_counter

    def mark_completed(self):
        """
        Marks the task as completed.
        """
        self.status = '已完成'

    def __str__(self):
        """
        String representation of the TodoListItem.

        Returns:
            str: String representation of the task.
        """
        return f"Task ID: {self.task_id}, Task: {self.task_name}, Status: {self.status}"
