from setuptools import setup, find_packages


__author__ = "James King"
__email__ = "james@agentultra.com"
__version__ = "0.1.1"
__license__ = "MIT"
__description__ = """
Ambit: the scope, extent, or bounds of something. A library for
manipulating ranges within a series.
"""


setup(
    name="Ambit",
    version=__version__,
    packages=find_packages(),

    install_requires = [
        "sphinx_bootstrap_theme", # for docs
    ],

    tests_require = {
        'nose',
    },
    test_suite = 'nose.collector',

    author=__author__,
    author_email=__email__,
    license=__license__,
    description=__description__,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
    ]
)
