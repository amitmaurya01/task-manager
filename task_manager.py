import os
import pickle


class Task:
    def __init__(self, task_id, description, completed=False) -> None:
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        status = "Completed" if self.completed else "Not Completed"
        return f"ID: {self.task_id} - Description: {self.description} - Status: {status}"

    def mark_as_completed(self):
        self.completed = True

    def mark_as_incomplete(self):
        self.completed = False


class TaskManager:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_completed()
                return True
        return False

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for task in self.tasks:
                print(task)

    def save_tasks_to_file(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks_from_file(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as file:
                self.tasks = pickle.load(file)
