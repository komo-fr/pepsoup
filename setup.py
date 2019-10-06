import os
from setuptools import setup, find_packages


def read_file(file_name):
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, file_name)
    if os.path.exists(file_path):
        return open(file_path).read()
    else:
        return ""


setup(
    name="pepsoup",
    version="0.0.1",
    packages=find_packages(),
    description="a package for data preprocessing to analyze PEPs",
    long_description=read_file("README.rst"),
    author="komo_fr",
    author_email="komo.mdrms@gmail.com",
    url="https://github.com/komo-fr/pepsoup",
    include_pakcages_data=True,
    install_requires=["beautifulsoup4"],
)
