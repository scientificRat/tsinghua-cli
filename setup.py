import setuptools


with open("README.md", 'r', encoding='utf8') as f:
    long_description = f.read()

setuptools.setup(
    name="tsinghua_cli",
    version="1.0.0",
    author="Zhengyue Huang",
    author_email="hzy18@mails.tsinghua.edu.cn",
    description="Tsinghua TUNet CLI connection tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    packages=setuptools.find_packages(),
    license="http://www.apache.org/licenses/LICENSE-2.0",
    install_requires=[],
    entry_points={
        'console_scripts': ['tsinghua_cli=tsinghua_cli.cli:main'],
    }
)
