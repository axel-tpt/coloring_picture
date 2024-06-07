from setuptools import setup, find_packages

setup(
    name='coloring_picture',
    version='1',
    packages=find_packages(),
    install_requires=[
        'pillow==10.3.0',
        'numpy==1.26.4',
        'scikit-learn==1.5.0',
    ],
    entry_points={
        'console_scripts': [
            'start=coloring.main:main',
        ],
    },
    author='Axel TREPOUT',
    author_email='axel.trepout@outlook.com',
    description='Create a coloring picture from a picture',
    url='https://github.com/axel-tpt/coloring_picture.git',
)