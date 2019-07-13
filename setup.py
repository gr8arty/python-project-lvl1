import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gr8arty_brain_games",
    version="0.1.0",
    author="gr8arty",
    author_email="gr8arty@gmail.com",
    description="Hexlet python project#1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gr8arty/python-project-lvl1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
