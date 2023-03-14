from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(file_path,"r+") as file_obj:
        requirements = file_obj.readlines()
        # remove \n from requirements
        requirements = [each_req.replace("\n","") for each_req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="Generic_ML_Project",
    version = "0.0.1",
    author="Aayushi",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt")
)