import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dirtools2",
    version="0.2.16",
    author="otapi",
    description="Exclude/ignore files in a directory (using .gitignore like syntax), compute hash, search projects for an entire directory tree and gzip compression.",
    license="MIT",
    keywords="exclude exclusion directory hash compression gzip",
    url="https://github.com/otapi/dirtools2",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["globster"],
    tests_require=["pyfakefs"],
    test_suite="test_dirtools",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
