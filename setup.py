from setuptools import setup, find_packages
from pathlib import Path

root = Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (root / "README.rst").read_text(encoding="utf-8")

setup(
    name="pkg-template-mh",
    version="1.1.3",
    description="Python package template with Github Actions CI/CD",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/hanicinecm/template-python-package/",
    author="Martin Hanicinec",
    author_email="hanicinecm@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing :: Unit",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    keywords="template python package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "pandas>=1.3.4",
    ],
    extras_require={
        "dev": ["pytest-cov", "tox", "black"],
    },
    project_urls={
        "Bug Reports": "https://github.com/hanicinecm/template-python-package/issues",
    },
)
