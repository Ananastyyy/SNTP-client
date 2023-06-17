import sys

import app

# Запускаем утилиту
if __name__ == '__main__':
    try:
        app.run()
    except PermissionError:
        sys.exit(7)
