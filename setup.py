from setuptools import find_packages, setup
setup(
    name='Probably',
    packages=find_packages(include=['Probably']),
    version='0.1.0',
    description='Library for basic probability functions',
    author='M4K4TT4CK',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)