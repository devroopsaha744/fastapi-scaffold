from setuptools import setup, find_packages

setup(
    name="fastapi-scaffold",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "fastapi-scaffold = fastapi_scaffold.cli:cli",
        ],
    },
    include_package_data=True,
    author="Devroop Saha",
    author_email="devroopsaha844@gmail.com",
    description="A CLI tool to scaffold FastAPI projects with ML, DB, Auth, and Docker options.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/devroopsaha744/fastapi-scaffold",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
