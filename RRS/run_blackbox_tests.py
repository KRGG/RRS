import os
import robot
import RRS.settings
from processwrapper import run_process
from django.conf import settings
from django.core.wsgi import get_wsgi_application

def run_wsgi():
    import RRS.wsgi

if __name__ == '__main__':
    
    run_wsgi()
    
    with run_process('python manage.py runserver'):
        for f in os.listdir('blackbox_tests'):
            if os.path.splitext(f)[1] == '.robot':
                robot.run('blackbox_tests/{}'.format(f))