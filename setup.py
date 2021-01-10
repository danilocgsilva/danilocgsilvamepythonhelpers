from setuptools import setup

VERSION = "1.1.0"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="danilocgsilvame-python-helpers",
    version=VERSION,
    description="General helpers to use in Python command line utilities",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="Python helpers command-line",
    url="https://github.com/danilocgsilva/danilocgsilvamepythonhelpers",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["danilocgsilvame_python_helpers"],
    include_package_data=True
)

