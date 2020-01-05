import setuptools

with open("README.md", "r") as rh:
    long_description = fh.read()

# TODO list of packages that are required
setuptools.setup(
    name='cover-art-completer'
    version='0.1'
    scripts=['cover-art-completer'],
    author="Jack Stinson",
    description="Recursively downloads cover art for your music library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackcstinson/cover-art-completer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)