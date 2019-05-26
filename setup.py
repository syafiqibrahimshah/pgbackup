from setuptools import find_packages, setup

with open('README.md', 'r'):
	long_description = f.read()

setup(
	name='pgbackup',
	version='0.1.0',
	author='Syafiq Ibrahim Shah',
	author_email='syafiqibrahimshah@gmail.com',
	description='A utility for backing up PostgreSQL database',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/syafiqibrahimshah/pgbackup',
	packages=find_packages('src')
)
