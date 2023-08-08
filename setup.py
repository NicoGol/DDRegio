from setuptools import setup, find_packages

setup(
    name="DDRegio",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas~=1.3.2",
        "geopandas~=0.6.1",
        "scikit-learn~=0.24.2",
        "numpy~=1.20.3",
        "scipy~=1.7.1",
        "regiorust~=0.1.0",
        "matplotlib~=3.4.2"
    ],
    entry_points={
        "console_scripts": [
            # If your project has command-line scripts, add their entry points here, e.g.
            # "my_script=my_package.my_module:main",
        ],
    },
    python_requires=">=3.6",
    # Add metadata about your project
    author="Nicolas Golenvaux",
    author_email="nicolas.golenvaux@uclouvain.be",
    description="A Branch-and-Bound Approach Using Decision Diagrams for Regionalization",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/NicoGol/DDRegio",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)