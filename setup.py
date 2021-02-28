import setuptools


try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except UnicodeDecodeError:
    with open("README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

with open('dev_up/const.py', 'r', encoding='utf-8') as f:
    exec(f.read())

setuptools.setup(
    name="dev_up",
    version=locals()['__version__'],
    author=locals()['__author__'],
    description=locals()['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url=locals()['__url__'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "pydantic", "aiohttp", "attrdict"],
    include_package_data=True,
)
