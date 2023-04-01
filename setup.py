from setuptools import setup, find_packages

setup(
    name='betterpyhap',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
          'cryptography',
        'ed25519',
        'zeroconf',
    ],
    extras_require={
        'QRCode': ['pyqrcode', 'base36'],
    },
    package_data={
        'betterpyhap': ['resources/*'],
    },
    author='jokubas noruisis',
    author_email='noruisis.jokubas@example.com',
    description='A Python implementation of the HomeKit Accessory Protocol (HAP)',
    url='https://github.com/jkubas/betterpyhap/blob/main/README.md',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
