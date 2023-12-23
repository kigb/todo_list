from todo_list import TodoList
from datetime import datetime
import argparse
from designed_output import todo_output
"""
    Add a new task to the todo list.
"""
def add_command(subparsers):
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('--task', type=str, help='Task description')
    # add_parser.add_argument('--starttime', type=str, help='Start time for the task, for example: 2023-12-13')
    add_parser.add_argument('--duetime', type=str, help='Due time for the task, format is XXXX-XX-XX, for example: 2023-12-13, the start time is current date')
    add_parser.add_argument('--priority', type=int, help='Priority of the task, it is 0 by default')  

"""
    Delete a task from the todo list.
"""
def delete_command(subparsers):
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('--id', type=int, help='ID of the task to delete')

"""
    Dump a task from the todo list.
"""
def dump_command(subparsers):
    dump_parser = subparsers.add_parser('dump', help='Dump a certain task')
    dump_parser.add_argument('--id', type=int, help='ID of the task to dump')

"""
    Complete a task from the todo list.
"""
def complete_command(subparsers):
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('--id', type=int, help='ID of the task to complete')

"""
    Show tasks for a specific date.
"""
def showdate_command(subparsers):
    showdate_parser = subparsers.add_parser('showdate', help='Show tasks for a specific date')
    showdate_parser.add_argument('--date', type=str, help='Date to show tasks for')

"""
    Show all tasks.
"""
def showall_command(subparsers):   
    showall_parser = subparsers.add_parser('showall', help='Show all tasks')

"""
    Show unfinished tasks.
"""
def showunfinished_command(subparsers):
    showunfinished_parser = subparsers.add_parser('showunfinished', help='Show unfinished tasks')

"""
    Merge tasks from previous dates into the specified date.
"""
def merge_command(subparsers):
    merge_parser = subparsers.add_parser('merge', help='Merge tasks from previous dates into the specified date')
    merge_parser.add_argument('--date', type=str, help='Date to merge tasks into, which means merge all unfinished tasks before to the certain date, format is XXXX-XX-XX, for example: 2023-12-13')

"""
    Add all commands to the parser.
"""
def Command_Add(subparsers):
    add_command(subparsers)
    delete_command(subparsers)
    dump_command(subparsers)
    complete_command(subparsers)
    showdate_command(subparsers)
    showall_command(subparsers)
    showunfinished_command(subparsers)
    merge_command(subparsers)

"""
    Parse the command line arguments and call the corresponding functions.
""" 
def parse_command(args,todolist):
    if args.command == 'add':
        # start_date_str = args.starttime
        # #turn date_str into 3 int
        # start_date_list = start_date_str.split('-')
        # start_date_list = [int(x) for x in start_date_list]
        # startdate = datetime(start_date_list[0],start_date_list[1],start_date_list[2])
        due_date_str = args.duetime
        #turn date_str into 3 int
        due_date_list = due_date_str.split('-')
        due_date_list = [int(x) for x in due_date_list]
        duedate = datetime(due_date_list[0],due_date_list[1],due_date_list[2])
        if args.priority == None:
            args.priority = 0
        todolist.add(args.task,duedate,args.priority)
    elif args.command == 'delete':
        todolist.delete_task_item(args.id)
    elif args.command == 'dump':
        todolist.dump_task_item(args.id)
    elif args.command == 'complete':
        todolist.finish_task_item(args.id)
    elif args.command == 'showdate':
        date_str = args.date
        #turn date_str into 3 int
        date_list = date_str.split('-')
        date_list = [int(x) for x in date_list]
        date = datetime(date_list[0],date_list[1],date_list[2])
        todo_output()
        todolist.show_date_tasks(date)
    elif args.command == 'showall':
        todo_output()
        print(todolist)
    elif args.command == 'showunfinished':
        todolist.show_all_unfinished_task()
    elif args.command == 'merge':
        date_str = args.date
        #turn date_str into 3 int
        date_list = date_str.split('-')
        date_list = [int(x) for x in date_list]
        date = datetime(date_list[0],date_list[1],date_list[2])
        todolist.merge(date)
    else:
        print('Unknown command: {}'.format(args.command))
        return False
    return True


"""
    Main function for the todo list manager.
"""
def main():
    todolist = TodoList()
    todolist.restore("todolist.log")
    parser = argparse.ArgumentParser(description='Todo List Manager')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    Command_Add(subparsers)
    args = parser.parse_args()
    parse_command(args,todolist)
    todolist.save("todolist.log")

    

if __name__ == '__main__':
    main()
