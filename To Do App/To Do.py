
import json

FILE_NAME = 'todos.json'


def load_tasks():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print('\nNo tasks found.')
        return

    print('\n=== TODO LIST ===')

    for i, task in enumerate(tasks, start=1):
        status = '✓' if task['done'] else '✗'
        print(f"{i}. [{status}] {task['title']}")


def show_completed_tasks(tasks):
    completed = [task for task in tasks if task['done']]

    if not completed:
        print('\nNo completed tasks.')
        return

    print('\n=== COMPLETED TASKS ===')

    for i, task in enumerate(completed, start=1):
        print(f"{i}. [✓] {task['title']}")


def show_pending_tasks(tasks):
    pending = [task for task in tasks if not task['done']]

    if not pending:
        print('\nNo pending tasks.')
        return

    print('\n=== PENDING TASKS ===')

    for i, task in enumerate(pending, start=1):
        print(f"{i}. [✗] {task['title']}")


def add_task(tasks):
    task = input('Enter task: ').strip()

    if not task:
        print('Task cannot be empty.')
        return

    tasks.append({
        'title': task,
        'done': False
    })

    save_tasks(tasks)
    print('Task added successfully.')


def remove_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input('Task number to remove: ')) - 1

        removed_task = tasks.pop(index)

        save_tasks(tasks)

        print(f"Removed: {removed_task['title']}")

    except (ValueError, IndexError):
        print('Invalid task number.')


def edit_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input('Task number to edit: ')) - 1

        new_task = input('New task text: ').strip()

        if not new_task:
            print('Task cannot be empty.')
            return

        tasks[index]['title'] = new_task

        save_tasks(tasks)

        print('Task updated successfully.')

    except (ValueError, IndexError):
        print('Invalid task number.')


def mark_complete(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input('Task number to mark complete: ')) - 1

        tasks[index]['done'] = True

        save_tasks(tasks)

        print('Task marked as completed.')

    except (ValueError, IndexError):
        print('Invalid task number.')


def mark_incomplete(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input('Task number to mark incomplete: ')) - 1

        tasks[index]['done'] = False

        save_tasks(tasks)

        print('Task marked as pending.')

    except (ValueError, IndexError):
        print('Invalid task number.')


def search_tasks(tasks):
    keyword = input('Enter keyword to search: ').strip().lower()

    if not keyword:
        print('Search cannot be empty.')
        return

    found = []

    for task in tasks:
        if keyword in task['title'].lower():
            found.append(task)

    if not found:
        print('No matching tasks found.')
        return

    print('\n=== SEARCH RESULTS ===')

    for i, task in enumerate(found, start=1):
        status = '✓' if task['done'] else '✗'
        print(f"{i}. [{status}] {task['title']}")


def main():
    tasks = load_tasks()

    while True:
        print('\n===== TODO APP =====')
        print('1. Show All Tasks')
        print('2. Add Task')
        print('3. Remove Task')
        print('4. Edit Task')
        print('5. Mark Complete')
        print('6. Mark Incomplete')
        print('7. Show Completed Tasks')
        print('8. Show Pending Tasks')
        print('9. Search Tasks')
        print('10. Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            show_tasks(tasks)

        elif choice == '2':
            add_task(tasks)

        elif choice == '3':
            remove_task(tasks)

        elif choice == '4':
            edit_task(tasks)

        elif choice == '5':
            mark_complete(tasks)

        elif choice == '6':
            mark_incomplete(tasks)

        elif choice == '7':
            show_completed_tasks(tasks)

        elif choice == '8':
            show_pending_tasks(tasks)

        elif choice == '9':
            search_tasks(tasks)

        elif choice == '10':
            print('Goodbye!')
            break

        else:
            print('Invalid option.')


if __name__ == '__main__':
    main()

