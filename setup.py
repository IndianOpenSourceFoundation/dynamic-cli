import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

DEPENDENCIES = []

setuptools.setup(
    name="dynamic",
    version="0.0.1",
    description="Search for your questions in stackoverflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IndianOpenSourceFoundation/dynamic-cli",
    packages=setuptools.find_packages(),
    install_requires=DEPENDENCIES,
    entry_points={"console_scripts": ['dynamic=main:search_obj.search_args']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)