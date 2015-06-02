import os
import robot
from processwrapper import run_process

def run_wsgi():
    import RRS.wsgi

if __name__ == '__main__':
    
    run_wsgi()
    
    with run_process('python manage.py testserver test_dedicated_data.json'):
        robot.run('blackbox_tests')
    