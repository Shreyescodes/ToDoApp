import platform
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox

# Import permissions for Android
if platform.system() == "Android":
    from android.permissions import request_permissions, Permission  # type: ignore
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

from database import Database

# Initialize db instance
db = Database()

class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk

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

    def delete_item(self, the_list_item):
        self.parent.remove_widget(the_list_item)
        db.delete_task(the_list_item.pk)

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

class MainApp(MDApp):
    task_list_dialog = None

    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.accent_palette = "Red"  # Accent color
        self.theme_cls.accent_hue = "500"  # Accent color shade

    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create New Task",
                type="custom",
                content_cls=DialogContent(),
                auto_dismiss=False
            )
        self.task_list_dialog.open()

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    def add_task(self, task, task_date):
        created_task = db.create_task(task.text, task_date)
        self.root.ids['incomplete_container'].add_widget(
            ListItemWithCheckbox(pk=created_task[0], text='[b]' + created_task[1] + '[/b]', secondary_text=created_task[2])
        )
        task.text = ''

    def show_incomplete_tasks(self):
        self.root.ids.incomplete_tasks_view.height = 400
        self.root.ids.completed_tasks_view.height = 0

    def show_completed_tasks(self):
        self.root.ids.incomplete_tasks_view.height = 0
        self.root.ids.completed_tasks_view.height = 400

    def on_start(self):
        try:
            completed_tasks, incomplete_tasks = db.get_tasks()

            for task in incomplete_tasks:
                add_task = ListItemWithCheckbox(pk=task[0], text=task[1], secondary_text=task[2])
                self.root.ids['incomplete_container'].add_widget(add_task)

            for task in completed_tasks:
                add_task = ListItemWithCheckbox(pk=task[0], text='[s]' + task[1] + '[/s]', secondary_text=task[2])
                add_task.ids.check.active = True
                self.root.ids['completed_container'].add_widget(add_task)

            # Initially, only show the incomplete tasks
            self.show_incomplete_tasks()

        except Exception as e:
            print(e)
            pass

if __name__ == '__main__':
    app = MainApp()
    app.run()
