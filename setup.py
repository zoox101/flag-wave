from setuptools import setup

DESCRIPTION = "Create a gif of a dude waving a flag."
with open("README.md","r") as f:
    LONG_DESCRIPTION = f.read()


with open("requirements.txt","r") as f:
    dependencies = f.read().splitlines()


setup(
    name="FlagWaver",
    version="0.0.57",
    description=DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    url="https://github.com/ShahriyarShawon/flag-wave",
    author="Shahriyar Shawon",
    author_email="ShahriyarShawon321@gmail.com",
    license="Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International",
    packages = [
        "FlagWaver"
    ],
    classifiers = [
        "Programming Language :: Python :: 3"
    ],
    install_requires = dependencies

)