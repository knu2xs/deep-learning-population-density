from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='deep_learning_population_density',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Using deep learning to estimate population density from aerial imagery.',
    long_description=long_description,
    author='Esri Advanced Analytics',
    license='Apache 2.0',
)
