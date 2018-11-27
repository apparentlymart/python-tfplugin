
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="tfplugin",
    version="dev",
    author="Martin Atkins",
    author_email="mart@degeneration.co.uk",
    description="Implement Terraform plugins in Python",

    packages=['tfplugin'],
    install_requires=[
        'protobuf>=3.6.1',
    ],
    setup_requires=[
        'nose>=1.0',
    ],
    tests_require=[
        'nose>=1.0',
        'coverage',
        'mock',
        'pep8',
    ],
    test_suite='nose.collector',

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)
