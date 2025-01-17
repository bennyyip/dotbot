import re
from os import path

from setuptools import find_packages, setup

here = path.dirname(__file__)


with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def read(*names, **kwargs):
    with open(path.join(here, *names), encoding=kwargs.get("encoding", "utf8")) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="dotbot",
    version=find_version("dotbot", "__init__.py"),
    description="A tool that bootstraps your dotfiles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anishathalye/dotbot",
    author="Anish Athalye",
    author_email="me@anishathalye.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
    keywords="dotfiles",
    packages=find_packages(),
    setup_requires=[
        "setuptools>=38.6.0",
        "wheel>=0.31.0",
    ],
    install_requires=[
        "PyYAML>=6.0.1,<7",
    ],
    extras_require={
        "dev": {
            "pytest",
            "tox",
        }
    },
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": [
            "dotbot=dotbot:main",
        ],
    },
)
