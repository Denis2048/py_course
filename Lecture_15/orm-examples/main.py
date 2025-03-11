import peewee
import datetime

db = peewee.SqliteDatabase("todo.db")

class Task(peewee.Model):
    task_name = peewee.CharField()
    task_priority = peewee.IntegerField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = "tasks"


Task.create_table()


# note1 = Task.create(task_name="Went to the cinema", task_priority=10)
# note1.save
#
# note2 = Task.create(task_name="Exercised in the morning", task_priority=11)
# note2.save
#
# note3 = Task.create(task_name="Worked in the garden", task_priority=4)
# note3.save
#
# note4 = Task.create(task_name="Listened to music", task_priority=66)
# note4.save


# tasks = Task.select()
#
# for task in tasks:
#     print(f"ID {task.id}: Task:{task.task_name} has {task.task_priority} priority")


# task = Task.get_by_id(5)     # 1 ID not found
# print(f"ID {task.id}: Task:{task.task_name} has {task.task_priority} priority")


# tasks = Task.select().where(Task.id > 2)
# for task in tasks:
#     print(f"ID {task.id}: Task:{task.task_name} has {task.task_priority} priority")
#
# print()
#
# tasks = Task.select().where(Task.task_priority > 10)
# for task in tasks:
#     print(f"ID {task.id}: Task:{task.task_name} has {task.task_priority} priority")
#
# print()


# tasks = Task.select().where((Task.id > 5) & (Task.id < 8))
# for task in tasks:
#     print(f"ID {task.id}: Task:{task.task_name} has {task.task_priority} priority")
# print()


# tasks = Task.select().limit(2)
#
# for task in tasks:
#     print(f"ID {task.id}: Task:{task.task_name} has {task.task_priority} priority")


# tasks = Task.select().limit(3)
# print(tasks.sql())


# tasks = Task.select().order_by(Task.created.desc())
#
# for task in tasks:
#     print(f"ID {task.id}: Task:{task.task_name} has {task.task_priority} priority")
#
# print()
# tasks = Task.select().order_by(Task.id.desc())
#
# for task in tasks:
#     print(f"ID {task.id}: Task:{task.task_name} has {task.task_priority} priority")


# Task.delete_by_id(5)
# query = Task.delete().where(Task.task_priority > 10)
# _ = query.execute()


# query = Task.update(task_name="RUN RUN RUN FOREST!").where(Task.id == 7)
# _ = query.execute()
