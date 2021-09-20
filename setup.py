import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="github-track",
    version="0.0.1",
    py_modules=["GhTrack"],
    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Lacina ZINA",

    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

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