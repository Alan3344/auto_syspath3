import os
import shutil
from setuptools import setup

# rmdir build dir
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CUR_PATH, 'build')
if os.path.isdir(path):
    print('INFO del dir ', path)
    shutil.rmtree(path)


setup(
    name='auto_syspath3',
    author='Alan3344',
    version='0.1',
    long_description=open('README.md', encoding='utf-8').read(),
    setup_requires=['pbr'],
    packages=['auto_syspath3'],
    include_package_data=True,
    exclude_package_data={
        '': [
            'build',
            'dist',
            '*.egg-info',
            '.eggs',
            '.github',
            '.git',
            '.idea',
            '.vscode',
            '*.pyc',
            '.DS_Store',
            '__pycache__',
            'venv',
        ],
    },
    install_requires=[],
    python_requires='>=3.6, <4',
)
