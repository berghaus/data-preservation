from setuptools import setup
from setuptools import setup, find_packages
packages = find_packages()

setup(
    name="Data Preservation",
    version="0.1.dev0",
    url="https://github.com/berghaus/data-preservation",
    author="DPHEP Collaboration",
    author_email="frank.berghaus@gmail.com",
    description="A service to make high energy physics data FAIR: finable, accessible, interoperable, and re-usable.",
    packages=packages,
    install_requires=[
        "Invenio>=2"
    ],
    entry_points={
        "invenio.config": [ "dphep=dphep.config" ]
    }
)
