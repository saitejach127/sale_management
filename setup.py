from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sale_management/__init__.py
from sale_management import __version__ as version

setup(
	name="sale_management",
	version=version,
	description="App to manage Sales of Catering companies",
	author="metamenu",
	author_email="metamenu@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
