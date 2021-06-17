import os
import shutil


class System:

    def __init__(self, path):
        self.path = path

    def main(self, command):

        if command == "help":
            return """
                "ls": "Вывод содержимого текущей папки на экран",
                "mkdir": "Создание папки",
                "delete": "Удаление папки или файла",
                "rename": "Переименовать папку или файл",
                "copy": "Копировать папку или файл",
                "stop": "Выключение сервера"
        """

        elif command == 'ls':
            try:
                directs = os.listdir(self.path)
                print(directs)
                return str(directs)[1:-1]
            except FileNotFoundError:
                return "File not found"
            except NotADirectoryError:
                return "Directory not found"

        elif command[:5] == 'mkdir':
            try:
                os.mkdir(self.path + '/' + command[6:])
                return "Done"
            except NotADirectoryError:
                return "Directory not found"
            except FileNotFoundError:
                return "Error"
            except OSError:
                return "Error"

        elif command[:6] == 'delete':
            try:
                if os.path.isdir(self.path):
                    os.rmdir(self.path)
                else:
                    os.remove(self.path)
            except OSError:
                return "Not found"

        elif command[:6] == 'rename':
            rename_objects = command.split(' ')
            try:
                os.rename(self.path + '/' + rename_objects[1], self.path + '/' + rename_objects[2])
                return "Done"
            except FileNotFoundError:
                return "Error"
            except IndexError:
                return "Error"
            except OSError:
                return "Error"

        elif command[:6] == "copy":
            copy_object = command.split(' ')
            if os.path.isdir(self.path):
                try:
                    shutil.move(copy_object[1], copy_object[2])
                except FileExistsError:
                    print('Такая папка там уже существует')
            else:
                shutil.move(copy_object[1], copy_object[2])

        else:
            return "None"

    def setPath(self, path):
        try:
            os.listdir(path)
            check = True
        except FileNotFoundError:
            check = False
        except NotADirectoryError:
            check = False
        except OSError:
            check = False

        if check:
            self.path = path
            return f"Home directory saved: {self.path}"
        else:
            return f"Not found directory: {path}"