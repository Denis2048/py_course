class Task:
    def __init__(self, task_id, task_name, task_prior):
        self.task_id = task_id
        self.task_name = task_name
        self.task_prior = task_prior

    def __str__(self):
        return f"ID: {self.task_id}, Name: {self.task_name}, Priority: {self.task_prior}\n"


class BadPriorityError(Exception):
    """Исключение для некорректного приоритета."""
    def __init__(self, task_prior, message="Приоритет задачи должен быть больше или равен 0"):
        self.task_prior = task_prior
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"BadPriorityError: {self.task_prior} -> {self.message}\n"


class BadIdError(Exception):
    """Исключение для некорректного ID задачи."""
    def __init__(self, task_id, message="ID задачи должен быть от 0 до 10"):
        self.task_id = task_id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"BadIdError: {self.task_id} -> {self.message}\n"


class BadNameError(Exception):
    """Исключение для некорректного имени задачи."""
    def __init__(self, task_name, message="Имя задачи должно содержать не менее 7 символов"):
        self.task_name = task_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"BadNameError: {self.task_name} -> {self.message}\n"


class TodoList:
    def __init__(self):
        self.tasks = {}

    def create(self, task_id, task_name, task_prior):
        """Создание задачи."""
        if task_prior < 0:
            raise BadPriorityError(task_prior)
        if task_id < 0 or task_id > 10:
            raise BadIdError(task_id)
        if len(task_name) < 7:
            raise BadNameError(task_name)

        self.tasks[task_id] = Task(task_id, task_name, task_prior)
        #print(f"\nЗадача создана: {self.tasks[task_id]}")
        print(f"\nЗадача создана")

    def update(self, task_id, task_name=None, task_prior=None):
        """Изменение задачи по ID."""
        if task_id in self.tasks:
            if task_name:
                if len(task_name) < 7:
                    raise BadNameError(task_name)
                self.tasks[task_id].task_name = task_name
            if task_prior:
                if task_prior < 0:
                    raise BadPriorityError(task_prior)
                self.tasks[task_id].task_prior = task_prior
            print("\nЗадача успешно обновлена!")
            print(f"ID: {self.tasks[task_id].task_id}, Name: {self.tasks[task_id].task_name}, Priority: \
{self.tasks[task_id].task_prior}")
        else:
            print(f"\nЗадача с ID {task_id} не найдена.")

    def delete(self, task_id):
        """Удаление задачи по ID."""
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Задача с ID {task_id} удалена.")
        else:
            print(f"Задача с ID {task_id} не найдена.")

    def read_all(self):
        """Вывод списка всех задач"""
        return [(task.task_id, task.task_name, task.task_prior) for task in self.tasks.values()]

    def find(self, task_id):
        """Поиск задачи по ID с выводом результата."""
        task = self.tasks.get(task_id, None)
        if task:
            print(f"Задача найдена: {task}")
        else:
            print(f"Задача с ID {task_id} не найдена.")
        return task
