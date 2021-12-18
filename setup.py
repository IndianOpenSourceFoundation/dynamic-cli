import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

DEPENDENCIES = ["rich", "simple-term-menu", "termcolor", "oauthlib", "requests-oauthlib", "selenium", "webdriver-manager"]
setuptools.setup(
    name="dynamic-cli",
    version="0.1.0",
    author="IOSF Community",
    author_email="ping@iosf.in",
    description="Search for your questions in stackoverflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IndianOpenSourceFoundation/dynamic-cli",
    project_urls={
        "Bug Tracker": "https://github.com/IndianOpenSourceFoundation/dynamic-cli/issues",
    },
    install_requires=DEPENDENCIES,
    package_dir={},
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ['dynamic=dynamic.__main__:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe = False,
)