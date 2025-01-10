from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='recombee-api-client',

    version='5.0.0',

    description='Client for Recombee recommendation API',
    long_description=long_description,

    url='https://github.com/Recombee/python-api-client',

    author='Recombee',
    author_email='ondrej.fiedler@recombee.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

    keywords='recommendation engine, recommender engine as a service, search, personalization, recombee, API client, machine learning',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[
        'requests>=2.20.0',
    ],

    python_requires='>=3.6',

    extras_require={},

    package_data={},

    entry_points={},
)
