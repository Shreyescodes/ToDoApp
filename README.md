# To-Do List Application
## Overview
This simple, user-friendly To-Do List application was built using KivyMD, a material design framework for Kivy. The application allows users to create, manage, and organize tasks with due dates, and keep track of completed and incomplete tasks.

## Features
Task Management: Add, edit, and delete tasks easily.
Due Dates: Assign due dates to tasks using an integrated date picker.
Task Completion: Mark tasks as complete or incomplete.
Task Persistence: All tasks are saved to an SQLite database, ensuring data persistence across sessions.
Material Design: Utilizes KivyMD for a clean, modern UI.

## Prerequisites
Python 3.x
Kivy==2.1.0
KivyMD==1.1.1
SQLite3 (included with Python)
sdl2_ttf==2.0.15
pillow

## Setup
1. Clone this repository:
```
git clone https://github.com/yourusername/todo-list-app.git
cd todo-list-app
```

2. Install the required Python packages:
```
pip install kivy kivymd
```

3. Run the application:
```
python main.py
```

## Usage
1. Adding Tasks: Click the "Add Task" button to open the task creation dialog. Enter the task details and select a due date.
2. Completing Tasks: Check the box next to a task to mark it as complete. The task will move to the "Completed" section.
3. Deleting Tasks: Swipe left on a task and click the delete icon to remove it from the list.

## Project Structure
main.py: The main application file where the Kivy app is initialized and the task management logic is handled.
database.py: Manages database operations such as creating tasks, marking tasks as complete, and deleting tasks.
main.kv: The Kivy language file defining the application's UI layout and design.

## Code Snippets
1. Adding a Task
```python
def add_task(self, task, task_date):
    created_task = db.create_task(task.text, task_date)
    self.root.ids['incomplete_container'].add_widget(
        ListItemWithCheckbox(pk=created_task[0], text='[b]' + created_task[1] + '[/b]', secondary_text=created_task[2])
    )
    task.text = ''
```

2. Marking a Task as Complete
```python
def mark(self, check, the_list_item):
    container = self.parent
    container.remove_widget(the_list_item)

    if check.active:
        the_list_item.text = '[s]' + the_list_item.text + '[/s]'
        db.mark_task_as_complete(the_list_item.pk)
        app.root.ids['completed_container'].add_widget(the_list_item)
    else:
        the_list_item.text = db.mark_task_as_incomplete(the_list_item.pk)
        app.root.ids['incomplete_container'].add_widget(the_list_item)
```

## Database Schema
The SQLite database contains a single table of tasks with the following schema:
id: Integer (Primary Key, Auto Increment)
task: Text (The task description)
due_date: Text (The due date for the task)
completed: Boolean (0 for incomplete, 1 for complete)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Feel free to submit issues or pull requests. Contributions are welcome!
