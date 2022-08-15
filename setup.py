from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.7'
DESCRIPTION = 'ZALANDO GDA SQL Server, PGSQL,CSV & JSON Connection Objects and Tools'

# Setting up
setup(
    name="gdastudio",
    version=VERSION,
    author="Kamil Martenczuk",
    author_email="<kamil.martenczuk@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pypyodbc', 'tqdm', 'colorama', 'psycopg2-binary'],
    keywords=['python', 'sql', 'csv', 'json'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
