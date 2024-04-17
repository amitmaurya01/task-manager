# Importing Task and TaskManager classes from task_manager.py
from task_manager import Task, TaskManager


def main():
    # Creating some tasks
    task1 = Task(1, "Complete assignment")
    task2 = Task(2, "Go to the gym")
    task3 = Task(3, "Buy groceries")

    # Creating a TaskManager instance
    task_manager = TaskManager()

    # Adding tasks to the TaskManager
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)

    # Viewing tasks before saving to file
    print("Tasks before saving:")
    task_manager.view_tasks()
    
    # Mark ID 1 task as completed
    task_manager.mark_task_as_completed(1)

    # Saving tasks to a file
    file_name = "tasks.pkl"
    task_manager.save_tasks_to_file(file_name)
    print(f"Tasks saved to {file_name}")

    # Creating a new TaskManager instance to load tasks
    new_task_manager = TaskManager()

    # Loading tasks from the file
    new_task_manager.load_tasks_from_file(file_name)
    print(f"\nTasks loaded from {file_name}:")

    # Viewing tasks after loading from file
    new_task_manager.view_tasks()


if __name__ == "__main__":
    main()
