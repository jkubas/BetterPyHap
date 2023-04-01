import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="betterpyhap",
    version="1.0.0",
    author="Jokubas Noruisis",
    author_email="noruisis.jokubas@gmail.com",
    description="A Python implementation of the HomeKit Accessory Protocol (HAP)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jkubas/BetterPyHap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    package_data={
        'betterpyhap': ['resources/*'],
    },
    python_requires='>=3.6',
)

)
