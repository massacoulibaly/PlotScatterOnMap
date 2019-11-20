# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:54:20 2019

@author: admin
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ensae2019",
    version="1.0",
    author="COULIBALY Massa, DJUFFO DJOUDA Sandra, KOUTYATE Cheick Oumar",
    author_email="massa.coulibaly@ensae.fr, sandra.djuffodjouda@ensae.fr, cheickoumar.kouyate@ensae.fr",
    description="A small example package for plot a scatter on a map",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabsens/Python-for-Data-Scientists-ENSAE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)