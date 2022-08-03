from setuptools import setup, find_packages
setup(
    name='mango',
    description='Guangxuan Xiao\'s Development Toolbox',
    packages=find_packages(exclude=['examples', 'tests']),
    license='MIT'
)
