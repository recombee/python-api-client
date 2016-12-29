from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='recombee-api-client',

    version='1.3',

    description='Client for Recombee recommendation API',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Recombee/python-api-client',

    # Author details
    author='Recombee',
    author_email='ondrej.fiedler@recombee.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='recommendation engine as a service',


    packages=find_packages(exclude=['contrib', 'docs', 'tests']),


    install_requires=['requests'],

    extras_require={},

    package_data={},

    data_files=[],

    entry_points={},
)
