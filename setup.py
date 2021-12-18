import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

DEPENDENCIES = [
    "certifi==2020.6.20",
    "chardet==3.0.4",
    "idna==2.10",
    "requests==2.24.0",
    "termcolor==1.1.0",
    "urllib3==1.26.5",
    "rich==9.9.0",
    "oauthlib==3.1.0",
    "requests-oauthlib==1.3.0",
    "colorama==0.4.4",
    "configparser==5.0.2",
    "crayons==0.4.0",
    "selenium==3.141.0",
    "webdriver-manager==3.3.0",
    "simple-term-menu==1.0.1",
]

setuptools.setup(
    name="dynamic-cli",
    version="1.0.0",
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
    entry_points={"console_scripts": ["dynamic=dynamic.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
