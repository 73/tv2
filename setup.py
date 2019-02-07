from setuptools import setup

setup(
    name="tv2",
    version="0.2.2-1",
    author="Sean Hammond, Vincent Perricone, Madison Scott-Clary",
    packages=["tv2"],
    scripts=["bin/tv2"],
    url="http://github.com/makyo/tv2/",
    license="GNU General Public License, Version 3",
    description="A fast note-taking app for the UNIX terminal",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "urwid==2.0.1",
        "chardet==3.0.4",
        ],
    classifiers=[
        'Programming Language :: Python :: 3',
        ],
)
