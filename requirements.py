# Using Python version : 3.9.2

import os

env_name = 'env'

# Upgrading global pip version
os.system('python3 -m pip install --upgrade pip')

# Creating new environment in pwd.
os.system(f'python3 -m venv {os.getcwd()}/{env_name}')

# Upgrading pip version of newly created environment.
os.system(f'{os.getcwd()}/{env_name}/bin/python3 -m pip install --upgrade pip')

# Installing packages in newly created environment.
# os.system(f'{os.getcwd()}/{env_name}/bin/python3 -m pip install --no-cache-dir --upgrade python-dotenv==0.21.0')
os.system(f'{os.getcwd()}/{env_name}/bin/python3 -m pip install --no-cache-dir --upgrade img2pdf==0.4.4')
os.system(f'{os.getcwd()}/{env_name}/bin/python3 -m pip install --no-cache-dir --upgrade Pillow==9.3.0')
os.system(f'{os.getcwd()}/{env_name}/bin/python3 -m pip install --no-cache-dir --upgrade fpdf==1.7.2')
os.system(f'{os.getcwd()}/{env_name}/bin/python3 -m pip install --no-cache-dir --upgrade PyPDF2==2.12.1')

os.system(f'{os.getcwd()}/{env_name}/bin/python3 -m pip install --no-cache-dir --upgrade twine==4.0.2')    # For uploading to PyPI
