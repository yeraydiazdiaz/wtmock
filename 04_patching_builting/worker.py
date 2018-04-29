import os


def work_on_env():
    path = os.path.join(os.getcwd(), os.environ['MY_VAR'])
    print(f'Working on {path}')
    return path

