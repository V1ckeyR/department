# Installation file telling Python how to install your project
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="department-pkg-V1ckeyR",
    version="0.0.1",
    author="Victoria Romanova",
    author_email="not.c0mp.uter.cat@gmail.com",
    description="A small project example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/V1ckeyR/department",
    project_urls={
        "Documentation": "https://github.com/V1ckeyR/department/tree/main/documentation",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "department-app"},
    packages=setuptools.find_packages(where="department-app"),
    python_requires=">=3.9",
)
