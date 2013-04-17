import subprocess

class Bash:

  def __init__(self):
    None

  def bash_command(self, cmd):
    p = subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out
