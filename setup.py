import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import setup, find_packages

if "install" in sys.argv[1]:

    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib"):
        lib_paths.append(get_python_lib(prefix="/usr/local/"))
    for path in lib_paths:
        existing_path = os.path.abspath(os.path.join(path, "sp"))
        if os.path.exists(existing_path):
            break

version = "1.0a0"

EXCLUDE_FROM_PACKAGES = ['']

setup(
    name="simpleparser",
    version=version,
    url="https://github.com/voldien/simpeparser",
    author="Valdemar Lindberg",
    author_email="voldiekami@gmail.com",
    description=open('README.md').read(),
    license="GNU General Public License v3 (GPLv3)",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: SP',
	'Intended Audience :: Developers'
        'License :: OSI Approved ::  GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],

)

