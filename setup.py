from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='betterpyhap',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    description='A Python implementation of the HomeKit Accessory Protocol (HAP)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jkubas/BetterPyHap',
    author='jokubas noruisis',
    author_email='noruisis.jokubas@example.com',
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
