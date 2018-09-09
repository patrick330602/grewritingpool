from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='grewritingpool',
    version='0.1.0',
    description='Helper for GRE Writing Pool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['grewritingpool'],
    author='callmepk',
    author_email='wotingwu@live.com',
    python_requires='>=3.5',
    scripts=['scripts/grewriting'],
    install_requires=[
          'lxml','beautifulsoup4','requests'
      ],
    keywords=['gre','writing'],
    url='https://github.com/patrick330602/grewritingpool'
)
