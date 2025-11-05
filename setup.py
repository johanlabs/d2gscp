from setuptools import setup, find_packages

setup(
    name="d2gscp",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "requests",
        "webdriver-manager",
    ],
    entry_points={
        "console_scripts": [
            "duckimg = d2gscp:main",
        ],
    },
)
