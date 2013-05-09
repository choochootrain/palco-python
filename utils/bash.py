import subprocess

class Bash:

  def __init__(self):
    None

  def run(self, cmd):
    p = subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out

  def fork(self, cmd):
    p = subprocess.Popen(['/bin/bash', '-c', cmd], stdin=None, stdout=None, stderr=None, close_fds=True)
