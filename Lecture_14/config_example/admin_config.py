import configparser


def main():
    config = configparser.ConfigParser()
    print(config.read("my_conf.ini"))

    admin = config["admin"]
    file_names = config["files"]
    print("ADMIN section:")
    print("User email: ", admin["usr_email"])
    print("User name:", admin["usr_name"])
    print("User password:", admin["usr_pass"])
    print()
    print("FILES section:")
    print("Old file:", file_names["source"])
    print("New file:", file_names["dist"])


if __name__ == "__main__":
    main()
