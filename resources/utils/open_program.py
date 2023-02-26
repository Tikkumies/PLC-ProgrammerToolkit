import subprocess

def open_program(command):
    subprocess.run(f'start "" "{command}"', shell=True, start_new_session=True) 