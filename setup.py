from os import getenv
from setuptools import setup

jai_lib_tag = "2022.2.24"
jai_lib_version = getenv("JAI_LIB", default=jai_lib_tag)

# 1st-party requirements:
install_requires = [
    (
        "jai_lib @ git+ssh://git@github.com/ominatechnologies/"
        f"jai_lib@{jai_lib_version}#egg=jai_lib&subdirectory=src/jai_lib"
    ),
]

setup(install_requires=install_requires)
