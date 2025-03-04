import pytest
from todo_module import Task, BadPriorityError, BadIdError, BadNameError, TodoList


class TestExceptions:
    def test_bad_priority_error(self):
        """Проверка исключения BadPriorityError."""
        with pytest.raises(BadPriorityError) as exc_info:
            raise BadPriorityError(-1)
        assert str(exc_info.value) == "BadPriorityError: -1 -> Приоритет задачи должен быть больше или равен 0\n"


class TestTodoList:
    """Тесты для класса TodoList."""
    @pytest.fixture
    def todo_list(self):
        """Фикстура для создания объекта TodoList."""
        return TodoList()

    def test_create_task(self, todo_list):
        """Проверка создания задачи."""
        todo_list.create(1, "Позвонить маме", 3)
        assert 1 in todo_list.tasks
        assert todo_list.tasks[1].task_name == "Позвонить маме"
        assert todo_list.tasks[1].task_prior == 3

    def test_create_task_invalid_id(self, todo_list):
        """Проверка создания задачи с некорректным ID."""
        with pytest.raises(BadIdError):
            todo_list.create(11, "Позвонить маме", 3)

    def test_create_task_invalid_name(self, todo_list):
        """Проверка создания задачи с некорректным именем."""
        with pytest.raises(BadNameError):
            todo_list.create(1, "Купить", 3)

    def test_update_task(self, todo_list):
        """Проверка обновления задачи."""
        todo_list.create(1, "Позвонить маме", 3)
        todo_list.update(1, task_name="Позвонить папе", task_prior=5)
        assert todo_list.tasks[1].task_name == "Позвонить папе"
        assert todo_list.tasks[1].task_prior == 5

    def test_read_all(self, todo_list):
        """Проверка вывода всех задач."""
        todo_list.create(1, "Позвонить маме", 3)
        todo_list.create(2, "Купить молоко", 1)
        tasks = todo_list.read_all()
        assert len(tasks) == 2
        assert (1, "Позвонить маме", 3) in tasks
        assert (2, "Купить молоко", 1) in tasks

    def test_find_task(self, todo_list):
        """Проверка поиска задачи."""
        todo_list.create(1, "Позвонить маме", 3)
        task = todo_list.find(1)
        assert task is not None
        assert task.task_name == "Позвонить маме"
