from setuptools import setup

import io
import os


version = '0.2.5'


readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
with io.open(readme_path, encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='markdown2ctags',
    description='Generates ctags-compatible output for the sections of a '
                'Markdown document.',
    long_description=long_description,
    license='BSD',
    author='John Szakmeister',
    author_email='john@szakmeister.net',
    url='https://github.com/jszakmeister/markdown2ctags',
    version=version,
    py_modules=['markdown2ctags'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'markdown2ctags = markdown2ctags:cli_main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Utilities',
    ]
)
