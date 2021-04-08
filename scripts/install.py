import sys
import subprocess

print('Downloading Necessary Packages...')
listOfPackages = ['PySimpleGUI', 'pycda', 'numpy', 'opencv-python']
for i in listOfPackages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    print('Completed Downloading', i)

print('Completed package downloading')