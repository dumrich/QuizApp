import subprocess

subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Merge directories'])
subprocess.run(['git', 'push', '-u', 'origin', 'master'])