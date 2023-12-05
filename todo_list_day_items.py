from todo_list_item import TodoListItem
import datetime
from datetime import datetime
class TodoListDayItems:
    """
    A class to represent a collection of TodoListItem objects for a specific day.

    Attributes:
        date (datetime): The date for which the todo_list is maintained.
        day_of_week (str): The day of the week.
        items (list): A list of TodoListItem objects.
    """

    def __init__(self, year, month, day):
        """
        Constructor for TodoListDayItems.

        Args:
            year (int): Year of the date.
            month (int): Month of the date.
            day (int): Day of the date.
        """
        self.date = datetime(year, month, day)
        self.day_of_week = self.date.strftime("%A")
        self.items = []

    def add_item(self, todo_item, position=0):
        """
        Adds a TodoListItem object to the items list at a specified position.

        Args:
            todo_item (TodoListItem): The TodoListItem object to be added.
            position (int): The position at which to insert the item. Defaults to 0,
                            which appends the item to the end of the list.
        """
        if position <= 0 or position > len(self.items):
            self.items.append(todo_item)
        else:
            self.items.insert(position - 1, todo_item)

    def remove_item(self, index):
        """
        Removes a TodoListItem object from the items list based on its index.

        Args:
            index (int): The index of the TodoListItem object to be removed.
        """
        if 0 <= index < len(self.items):
            del self.items[index-1]

    def __str__(self):
        """
        String representation of the TodoListDayItems.

        Returns:
            str: String representation of the TodoListDayItems.
        """
        items_str = "\n".join(f"Priority: {index + 1} {item}" for index, item in enumerate(self.items))
        return f"Date: {self.date.strftime('%Y-%m-%d')}, Day: {self.day_of_week}\nTasks:\n{items_str}"

# Example usage
# todo_day = TodoListDayItems(2023, 12, 5)  # Creating a TodoListDayItems for a specific date
# todo_day.add_item(TodoListItem("复习编译原理",datetime(2023,12,6)))  # Adding an item
# todo_day.add_item(TodoListItem("学习xyue",datetime(2023,12,5)), 1)  # Adding another item with highest priority
# todo_day.add_item(TodoListItem("学习 C++",datetime(2023,12,6)), 2)  # Adding another item with second highest priority
# # todo_day.remove_item(2)  # Removing an item
# print(todo_day)  # Displaying the TodoListDayItems

