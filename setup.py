from setuptools import setup, find_packages

setup(
    name='rasa_addons',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/Revmaker/rasa_addons',
    license='Apache 2.0',
    author='Cher Huang',
    author_email='cher@carlabs.com',
    description='Addons for Rasa',
    install_requires=["rasa", "nltk"]
)
