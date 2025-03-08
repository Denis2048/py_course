import logging

# Формат логов
FORMAT = "%(levelname)s - %(message)s"

logger = logging.getLogger("user activity")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("user_activity.log", mode="a")
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)

def decorate_user_activity(func):
    """Декоратор для логирования действий."""
    def int_wrapper(usr):
        message = f"User: {usr.name} {usr.surname}. Completed --> {func.__name__}"
        logger.debug(message)
        func(usr)
    return int_wrapper


class User:
    """Класс для представления пользователя."""
    def __init__(self, n, s):
        self.name = n
        self.surname = s

    # Метод для входа в систему.
    @decorate_user_activity
    def login(self):
        print("login")

    # Метод для смены пароля.
    @decorate_user_activity
    def change_password(self):
        print("change_password")
