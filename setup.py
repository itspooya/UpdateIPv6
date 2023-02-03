from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='dynamic_ip_update',
    version='1.0.0',
    author='Pooya',
    author_email='pooyadowlat@gmail.com',
    description='A script to update dynamic IP address in tunnel broker',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itspooya/UpdateIPv6",
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'dynamic_ip_update=app:main',
        ],
    },
)