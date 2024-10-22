# setup.py
from setuptools import setup, find_packages

setup(
    name='storacha-python-client',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    description='Python client for interacting with Storacha decentralized storage',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/storacha-python-client',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
