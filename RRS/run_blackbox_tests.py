import os
import robot
from processwrapper import run_process


if __name__ == '__main__':
    with run_process('python manage.py runserver'):
        for f in os.listdir('blackbox_tests'):
            if os.path.splitext(f)[1] == '.robot':
                robot.run('blackbox_tests/{}'.format(f))