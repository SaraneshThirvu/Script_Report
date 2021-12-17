from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in thirvusoft/__init__.py
from thirvusoft import __version__ as version

setup(
	name="thirvusoft",
	version=version,
	description="TS",
	author="TS",
	author_email="TS",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
