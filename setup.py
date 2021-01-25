import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redditmon",
    version="0.0.1",
    author="Chris Cummings",
    author_email="nouser@slash64.tech",
    description="A simple package for viewing reddit posts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cummings-chris/redditmon",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
