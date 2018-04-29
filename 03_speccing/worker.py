import os


class Helper:

    def __init__(self, path):
        self.path = path

    def get_folder(self):
        base_path = os.getcwd()
        return os.path.join(base_path, self.path)


class Worker:

    def __init__(self):
        self.helper = Helper('db')

    def work(self):
        path = self.helper.get_path()
        print(f'Working on {path}')
        return path
