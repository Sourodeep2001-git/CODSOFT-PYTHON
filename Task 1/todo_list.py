tasks = []
task_id_counter = 1

def add_task(description):
    global task_id_counter
    task = {'id': task_id_counter, 'description': description, 'status': 'incomplete'}
    tasks.append(task)
    task_id_counter += 1

def update_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            return True
    return False

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'complete'
            return True
    return False

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

def main():
    while True:
        command = input("Enter a command (add, update, complete, delete, list, quit): ").strip().lower()
        if command == 'add':
            description = input("Enter task description: ").strip()
            if description:
                add_task(description)
                print("Task added.")
            else:
                print("Description cannot be empty.")
        elif command == 'update':
            try:
                task_id = int(input("Enter task ID to update: ").strip())
                new_description = input("Enter new description: ").strip()
                if new_description and update_task(task_id, new_description):
                    print("Task updated.")
                else:
                    print("Task not found or invalid description.")
            except ValueError:
                print("Invalid task ID.")
        elif command == 'complete':
            try:
                task_id = int(input("Enter task ID to complete: ").strip())
                if complete_task(task_id):
                    print("Task marked as complete.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid task ID.")
        elif command == 'delete':
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                delete_task(task_id)
                print("Task deleted.")
            except ValueError:
                print("Invalid task ID.")
        elif command == 'list':
            list_tasks()
        elif command == 'quit':
            print("Exiting the application.")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
