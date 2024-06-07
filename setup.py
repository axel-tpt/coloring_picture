from setuptools import setup, find_packages

setup(
    name='coloring_picture',
    version='1',
    packages=find_packages(),
    install_requires=[
        'pillow==10.3.0',
    ],
    entry_points={
        'console_scripts': [
            'starts=coloring.main:main',
        ],
    },
    author='Axel TREPOUT',
    author_email='axel.trepout@outlook.com',
    description='*',
    url='*',
)