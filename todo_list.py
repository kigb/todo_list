from todo_list_day_items import TodoListDayItems
from todo_list_item import TodoListItem
import pickle
class TodoList:
    """
    A class to represent a todo_list with multiple TodoListDayItems.

    Attributes:
        day_items (list): A list of TodoListDayItems objects.
    """

    def __init__(self):
        """
        Constructor for TodoList.
        """
        self.day_items = []
        self.all_items = []

    def find_or_create_day_item(self, target_date):
        """
        Finds or creates a TodoListDayItems object for the given target_date.

        Args:
            target_date (date): The date for which to find or create a TodoListDayItems object.

        Returns:
            TodoListDayItems: The TodoListDayItems object for the target_date.
        """
        for index, day_item in enumerate(self.day_items):
            if day_item.date == target_date:
                return day_item
            elif day_item.date > target_date:
                new_day_item = TodoListDayItems(target_date.year, target_date.month, target_date.day)
                self.day_items.insert(index, new_day_item)
                return new_day_item

        # If target_date is greater than all existing dates, create a new day item at the end
        new_day_item = TodoListDayItems(target_date.year, target_date.month, target_date.day)
        self.day_items.append(new_day_item)
        return new_day_item

    def add(self, task_name, due_date, priority=0):
        """
        Adds a TodoListItem to the TodoList.

        Args:
            task_name (str): Name or description of the task.
            due_date (date): Due date of the task.
            priority (int): Priority of the task. Defaults to 0.
        """
        task_item = TodoListItem(task_name, due_date)
        day_item = self.find_or_create_day_item(due_date)
        day_item.add_item(task_item, priority)

        # Append the task to the array of all tasks
        self.all_items.append(task_item)

    def get_task_item(self, task_id):
        """
        Get a TodoListItem by its task ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            TodoListItem or None: The TodoListItem object with the specified ID, or None if not found.
        """
        for item in self.all_items:
            if item.task_id == task_id:
                return item
        return None

    def merge(self, target_date):
        """
        Merges unfinished tasks from previous dates into the specified date.

        Args:
            target_date (date): The target date to merge tasks into.
        """
        target_day_item = self.find_or_create_day_item(target_date)

        # Iterate through previous day items
        for day_item in self.day_items:
            if day_item.date < target_date:
                # Iterate through items in the previous day item
                for item in day_item.items:
                    if item.status == '未完成':
                        # Mark the item as completed and move it to the target day item
                        target_day_item.add_item(item)

    def show_all_unfinished_task(self):
        """
        Shows unfinished tasks from all initialized dates
        
        Args:
            None.

        Returns:
            the array of all unfinished tasks
        """
        unfinished = []
        print("当前未完成的task：")
        for task_item in self.all_items:
            if task_item.status == '未完成':
                print(task_item)
                unfinished.append(task_item)
        return unfinished

    def finish_task_item(self,task_id):
        """
        Finish the task whose task_id is input

        Args:
            task_id

        Returns:
            the result of finish operation(True or False)
        """
        cur_task_item = self.get_task_item(task_id)
        if cur_task_item is None:
            return False
        cur_task_item.status = '已完成'
        return True

    def save(self, filename):
        """
        Save the TodoList to a file.

        Args:
            filename (str): The name of the file to save to.
        """
        with open(filename, 'wb') as file:
            # 保存 all_items 列表中的任务项
            pickle.dump(self.all_items, file)
            # 保存每个日期对象，包括日期和其中的任务项的索引
            day_items_data = []
            for day_item in self.day_items:
                day_item_indices = [self.all_items.index(task) for task in day_item.items]
                day_item_data = {
                    'date': day_item.date,
                    'day_of_week': day_item.day_of_week,
                    'items_indices': day_item_indices
                }
                day_items_data.append(day_item_data)
            pickle.dump(day_items_data, file)

    def restore(self, filename):
        """
        Restore the TodoList from a file.

        Args:
            filename (str): The name of the file to restore from.
        """
        with open(filename, 'rb') as file:
            # 恢复 all_items 列表中的任务项
            self.all_items = pickle.load(file)
            # 恢复每个日期对象，包括日期和其中的任务项的索引
            day_items_data = pickle.load(file)
            self.day_items = []
            for day_item_data in day_items_data:
                date = day_item_data['date']
                day_of_week = day_item_data['day_of_week']
                items_indices = day_item_data['items_indices']

                # 根据索引从 all_items 中获取任务项
                items = [self.all_items[index] for index in items_indices]

                # 创建并添加日期对象
                day_item = TodoListDayItems(date.year, date.month, date.day)
                day_item.day_of_week = day_of_week
                day_item.items = items
                self.day_items.append(day_item)

    def __str__(self):
        """
        String representation of the TodoList.

        Returns:
            str: String representation of the TodoList.
        """
        return "\n".join(str(day_item) for day_item in self.day_items)

#test
todolist = TodoList()
# a = todolist.find_or_create_day_item(datetime(2020, 1, 1))
# b = todolist.find_or_create_day_item(datetime(2020, 1, 2))
# a.add_item(TodoListItem("复习编译原理",datetime(2023,12,6)))
# b.add_item(TodoListItem("复习编译原理1",datetime(2023,12,6)))
# todolist.merge(datetime(2023,12,6))
# print(todolist)
# todolist.add("kkkk",datetime(2023,12,5))
# todolist.add("复习编译原理1",datetime(2023,12,6))
# a = todolist.get_task_item(1)
# todolist.merge(datetime(2023,12,6))
# todolist.restore("todolist.log")
# #
# print(todolist)
# a = todolist.show_all_unfinished_task()
# todolist.finish_task_item(1)
# todolist.show_all_unfinished_task()
# print(todolist)
# todolist.save("todolist.log")