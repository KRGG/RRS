import os
import robot
from processwrapper import run_process


if __name__ == '__main__':
    with run_process('python manage.py runserver'):
        robot.run('blackbox_tests')
