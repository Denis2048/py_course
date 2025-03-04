from todo_module import TodoList, BadPriorityError, BadIdError, BadNameError


class App:
    def __init__(self):
        self.todo_list = TodoList()

    def Menu(self):
        print("=" * 30, end="")
        print("""
1. Создать задачу
2. Обновить задачу
3. Удалить задачу
4. Показать все задачи
5. Найти задачу
6. Выйти
""", end="")
        print("=" * 30)

    def Run(self):
        """Основная логика."""
        while True:
            self.Menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                print()
                try:
                    task_id = int(input("Введите ID задачи (0-10): "))
                    task_name = input("Введите имя задачи (минимум 7 символов): ")
                    task_prior = int(input("Введите приоритет задачи (>= 0): "))
                    self.todo_list.create(task_id, task_name, task_prior)
                except (BadPriorityError, BadIdError, BadNameError) as e:
                    print()
                    print(e)

            elif choice == "2":
                task_id = int(input("Введите ID задачи: "))
                task_name = input("Введите новое имя задачи (оставьте пустым, чтобы не изменять): ")
                task_prior = input("Введите новый приоритет задачи (оставьте пустым, чтобы не изменять): ")
                try:
                    self.todo_list.update(task_id,
                                          task_name if task_name else None,
                                          int(task_prior) if task_prior else None)
                except (BadPriorityError, BadNameError) as e:
                    print(e)

            elif choice == "3":
                task_id = int(input("Введите ID задачи: "))
                self.todo_list.delete(task_id)

            elif choice == "4":
                tasks = self.todo_list.read_all()
                if tasks:
                    print("Список всех задач:")
                    for task_id, task_name, task_prior in tasks:
                        print(f"ID: {task_id}, Name: {task_name}, Priority: {task_prior}")
                else:
                    print("\nЗадачи отсутствуют.")

            elif choice == "5":
                task_id = int(input("Введите ID задачи: "))
                self.todo_list.find(task_id)

            elif choice == "6":
                break

            else:
                print("\nНеверный выбор. Попробуйте снова.")
