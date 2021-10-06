import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='nvec',
    version='1.0.0',
    author='miir',
    author_email='itsmiir@outlook.com',
    description='vectors of n-dimensional size',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/itsmiir/pyvec',
    project_urls = {
        "Bug Tracker": "https://github.com/itsmiir/pyvec/issues"
    },
    license='MIT',
    packages=['nvec'],
    install_requires=['']
)
