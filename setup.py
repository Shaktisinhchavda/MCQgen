from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Shaktisinh Chavda",
    author_email="connectshaktisinh@gmail.com",
    install_requires = ["langchain","langchain-google-genai","streamlit","python-dotenv","PyPDF"],
    packages=find_packages()
    
)