import sqlite3


conn = sqlite3.connect("todo.db")
print(type(conn))

c = conn.cursor()
print(type(c))


# c.execute("""CREATE TABLE IF NOT EXISTS tasks (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );""")

# c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", ("My first task", 1))
# conn.commit()


# tasks = [
#     ("My new task", 15),
#     ("My second task", 5),
#     ("My third task", 10),
# ]
#
# c.executemany("INSERT INTO tasks (name, priority) VALUES (?,?)", tasks)
# conn.commit()


# for row in c.execute("SELECT * FROM tasks"):
#     print(row)


# c.execute("SELECT * FROM tasks")
# rows = c.fetchall()
# for row in rows:
#     print(row)


# c.execute("SELECT * FROM tasks")
# row = c.fetchone()
# print(row)
# row = c.fetchone()
# print(row)


# c.execute("UPDATE tasks SET priority = ? WHERE id = ?", (20, 1))
# conn.commit()


# c.execute("DELETE FROM tasks WHERE id = ?", (1,))
# conn.commit()
# conn.close()

# with sqlite3.connect("todo.db") as conn:
#     with conn.cursor() as c:
#         c.execute("""CREATE TABLE IF NOT EXISTS tasks (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         priority INTEGER NOT NULL
#         );""")
#
#     c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", ("My first task", 1))
#
#     conn.commit()

