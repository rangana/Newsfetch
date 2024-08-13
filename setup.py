'''Setup.'''

import setuptools

DIST_NAME = 'Newsfetch'
version = '2.8.3'

setuptools.setup(
    name='%s-nuuuwan' % DIST_NAME,
    version=version,
    author='Rangana Sampath',
    author_email='nzrangana@gmail.com',
    description='A simple API to fetch data from Sri Lankan newspapers.',
    long_description='',
    long_description_content_type='text/markdown',
    url='https://github.com/rangana/%s' % DIST_NAME,
    project_urls={
        'Bug Tracker': 'https://github.com/rangana/%s/issues' % DIST_NAME,
    },
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: The Unlicense',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
        'bs4',
        'pytest',
        'selenium',
        'utils-nuuuwan',
        'spacy',
        'fuzzywuzzy',
        'matplotlib',
        'wordcloud',
        'python-Levenshtein',
        'imageio',
        'moviepy',
        'numpy',
    ],
)
