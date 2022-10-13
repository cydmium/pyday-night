import setuptools


import versioneer

with open("README.md", "r") as f:
    long_description = f.read()
with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f]

setuptools.setup(
    name="pyday-night",
    description="Tools for working with the Day-Night Terminator",
    long_description=long_description,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="David Richardson",
    author_email="drichardson42@gatech.edu",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=["pydaynight"]),
    install_requires=requirements,
    extras_require={"dev": ["twine"], "test": ["pytest"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
    ],
)
