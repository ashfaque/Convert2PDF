# Using Python version : 3.9.2

env_name = 'myenv'

pkgs_list = [
    'img2pdf==0.4.4'
    , 'Pillow==9.3.0'
    , 'fpdf==1.7.2'
    , 'PyPDF2==2.12.1'
    , 'twine==4.0.2'    # For uploading to PyPI
    # , 'python-dotenv==0.21.0'

]

# ##############################################################################################################

import os
from sys import platform
from multiprocessing import Process


if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
    python = 'python3'
    bin_name = 'bin'
elif platform == 'win32':
    python = 'python'
    bin_name = 'Scripts'
else:
    python = 'python3'
    bin_name = 'bin'



pwd = os.getcwd()

# Upgrading global pip version
os.system(f"{python} -m pip install --upgrade pip")

# Creating new environment in pwd.
os.system(f"{python} -m venv {os.path.join(pwd, env_name)}")

# Upgrading pip version of newly created environment.
os.system(f"{os.path.join(pwd, env_name, bin_name, python)} -m pip install --upgrade pip")

# Installing packages in newly created environment.
def install_pkgs(pwd, env_name, bin_name, python, pkg):
    os.system(f"{os.path.join(pwd, env_name, bin_name, python)} -m pip install --no-cache-dir --upgrade {pkg}")

for pkg in pkgs_list:
    # os.system(f"{os.path.join(pwd, env_name, bin_name, python)} -m pip install --no-cache-dir --upgrade {pkg}")
    p = Process(target=install_pkgs, args=(pwd, env_name, bin_name, python, pkg))
    p.start()
