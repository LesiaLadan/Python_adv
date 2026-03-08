from typing import Any


def create_user_settings():
    """Creates a closure that stores user settings and allows updating them"""
    settings = {"theme": "light", "language": "en", "notifications": True}

    def change_settings(**kwargs) -> dict[str, Any]:
        """Updates user settings with the given keyword arguments"""
        for key, value in kwargs.items():
            settings[key] = value
        return settings

    return change_settings


if __name__ == "__main__":

    user_settings = create_user_settings()
    print(user_settings())
    user_settings(theme="dark", language="ua")
    print(user_settings())
    user_settings(notifications=False)
    print(user_settings())
