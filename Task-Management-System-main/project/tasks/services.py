from .models import Task

class TaskService:
    @staticmethod
    def create_task(title, description=None):
        return Task.objects.create(title=title, description=description)

    @staticmethod
    def get_all_tasks(completed=None):
        if completed is not None:
            return Task.objects.filter(completed=completed)
        return Task.objects.all()

    @staticmethod
    def get_task_by_id(task_id):
        try:
            return Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return None

    @staticmethod
    def update_task(task_id, title=None, description=None, completed=None):
        task = TaskService.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if completed is not None:
                task.completed = completed
            task.save()
        return task

    @staticmethod
    def delete_task(task_id):
        task = TaskService.get_task_by_id(task_id)
        if task:
            task.delete()
            return True
        return False
