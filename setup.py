from setuptools import setup, find_packages

setup(
    name='storacha-python-client',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'storacha-client=src.storacha_client:main',
        ],
    },
)
