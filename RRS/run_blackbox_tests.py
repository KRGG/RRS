import os
import subprocess
import signal
import psutil
import robot

def kill_proc_tree(pid, including_parent=True):    
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        child.kill()
    if including_parent:
        parent.kill()

if __name__ == '__main__':
    server = subprocess.Popen(["python", "manage.py", "runserver"], stdout=subprocess.PIPE)
    
    for f in os.listdir('blackbox_tests'):
        if os.path.splitext(f)[1] == '.robot':
            robot.run('blackbox_tests/base_template_tests.robot')
    
    kill_proc_tree(server.pid)