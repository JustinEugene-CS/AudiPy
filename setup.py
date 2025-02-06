from setuptools import setup, find_packages

setup(
    name='AudiPy',
    version='0.8',
    description='A simple audio file reader',
    long_description='A simple audio file reader',
    author='Nick Stephens, Group 10 hackMT 2025',
    author_email='robert.nicholas.stephens@gmail.com',
    url='https://github.com/JustinEugene-CS/AudiPy',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'opencv-python'
                      ],
    # python_requires='>=3.6',
)


