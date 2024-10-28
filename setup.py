from setuptools import setup, find_packages

setup(
    name='gHangman',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    author='a-good-omen',
    author_email='student.rohn@gmail.com',
    description='A classical word guessing game.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/a-good-omen/hangman-remastered',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hangman=start:main',
        ],
    },
)