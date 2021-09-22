import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="github-track",
    version="0.0.1",
    py_modules=["GhTrack"],
    description="An Python module api app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zinaLacina/github-track",
    package_data="data/*",
    test_suite="tests",
    author="Lacina ZINA",

    package_dir={"": "ghtrack"},
    packages=setuptools.find_packages(where="ghtrack"),

    install_requires=[
        "",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: MIT License:: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)