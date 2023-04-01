from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='betterpyhap',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'async-timeout==4.0.2',
        'base36==0.1.1',
        'cffi==1.15.1',
        'chacha20poly1305-reuseable==0.0.4',
        'cryptography==40.0.1',
        'ed25519==1.5',
        'h11==0.14.0',
        'ifaddr==0.2.0',
        'orjson==3.8.9',
        'pycparser==2.21',
        'PyQRCode==1.2.1',
        'zeroconf==0.51.0'
    ],
    include_package_data=True,
    description='A Python implementation of the HomeKit Accessory Protocol (HAP)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jkubas/BetterPyHap',
    author='jokubas noruisis',
    author_email='noruisis.jokubas@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

