from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='image_scorify',
    version='1.0',
    description='Image Feature Scoring',
    long_description=readme,
    author='Peter Antonaros Jr.',
    url='https://github.com/peterantonarosjr/image_scorify',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)