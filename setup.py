import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-util",
    version="1.0.1",
    author="MisterL2",
    author_email="misterl2@gmx.net",
    description="A small python utilities addon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MisterL2/python-util",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
