# python setup.py install

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requiremens(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as path:
        requirements = path.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

# to ignore -e .
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name="DiabeticPricePrediction",
    version="0.0.1",
    author="Nick",
    author_email="nikhilsingxlx@gmail.com",
    install_requires=get_requiremens("requirements.txt"),
    packages=find_packages()

)
