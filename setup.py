from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file path.
    Args:
        file_path: Path to requirements.txt file
    Returns:
        List of requirements without -e .
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        
        # Remove -e . if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
        # Remove empty lines and comments
        requirements = [req for req in requirements if req and not req.startswith("#")]
    
    return requirements

setup(
    name="ml_project",
    version="0.0.1",
    author="Adan Jafri",
    author_email="adanabbasjafri@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

if __name__ == "__main__":
    # For debugging purposes only
    print("Package requirements:", get_requirements("requirements.txt"))