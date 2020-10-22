"""
Provides an easy way to configure git username on a per repository basis.
"""

from setuptools import setup, find_packages
import glob


setup(
    name='git-persona',
    version='1.0',

    install_requires=[
        'setuptools',
    ],

    author='Bastien MENNESSON <bastien.mennesson@pm.me>',
    author_email='bastien.mennesson@pm.me',
    license='BSD',
    url='https://github.com/bastienm/git-persona/',

    description=__doc__.strip(),
    long_description='\n\n'.join(open(name).read() for name in (
        'README.txt',
        'CHANGES.txt',
    )),

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('', glob.glob('*.txt'))],
    zip_safe=False,
)
