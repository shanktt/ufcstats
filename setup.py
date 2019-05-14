import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ufcstats",
    version="0.0.2",
    author="Ashank Kumar",
    author_email="ashankkumar01@gmail.com",
    description="A package to retrieve stats from ufcstats.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AshankKumar/UFCStats",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)