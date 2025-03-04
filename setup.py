from setuptools import find_packages, setup
from typing import List  # Import List for type hinting

HYPHEN = '-e.'

def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements from a file and return them as a list.
    
    Args:
        file_path (str): Path to the requirements file
    
    Returns:
        list: List of requirement strings
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Corrected list comprehension

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kenneth Pieterson',
    author_email='kenneth19p@yahoo.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') 
)