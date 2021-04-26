import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="simple-debugger",
    version="0.0.1",
    description="Simple Debugger for Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mzebin/simple-debgugger",
    author="Mohammed Zebin",
    packages=["simple_debugger"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)