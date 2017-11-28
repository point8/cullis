import os
from setuptools import setup

exec(compile(open('cullis/version.py', "rb").read(),
             'cullis/version.py',
             'exec'))


setup(
    name='cullis',
    description='cullis',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=['cullis'],
    version=__version__,
    entry_points={
        'console_scripts': [
            'cullis = cullis.cli:main',
        ]
    },
    package_data={
        'cullis': ['templates/*']
    },
    tests_require=['pytest', 'pytest-runner', 'pytest-cov'],
    setup_requires=['pytest-runner'],
    install_requires=['click', 'python-pptx', 'wand', 'pdfrw'],
)