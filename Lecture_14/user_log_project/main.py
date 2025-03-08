from module import User


def main():
    """Основная функция для тестирования."""
    for i in range(10):
        usr = User(f"Rick-{i}", "Morty")
        usr.login()
        usr.change_password()


if __name__ == "__main__":
    main()
