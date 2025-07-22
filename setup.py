from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECCOMENDER",
    version="0.1",
    author="ReeshmaRam",
    packages=find_packages(),
    install_requires = requirements,
)