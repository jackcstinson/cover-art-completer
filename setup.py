import setuptools

with open("README.md", "r") as rh:
    long_description = rh.read()

# TODO list of packages that are required
setuptools.setup(
    name='cover_completer',
    version='0.1',
    scripts=['cover_completer'],
    author="Jack Stinson",
    description="Recursively downloads cover art for your music library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackcstinson/cover_completer",
    packages=setuptools.find_packages(),
    install_requires=[
        'pylast',
        'tinytag',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'cover_completer = cover_completer.cli:main',
        ]
    }
)