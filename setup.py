import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="kquery",
    version="0.0.4",
    author="Felipe Ferreira",
    author_email="felipe.gomes.ferreira@gmail.com",
    description="Damn small QT based database client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samambaman/kquery",
    packages=setuptools.find_packages(),
    keywords='postgresql database client qt pyqt',
    classifiers=(
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ),
    install_requires=[
        "psycopg2-binary",
        "PyQt5"
    ],
    entry_points={
          "console_scripts": [
              "kquery = kquery.cli:cli",
          ],
      },
)
