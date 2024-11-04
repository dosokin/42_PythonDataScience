from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
        name="ft_package",
        version=VERSION,
        description="A sample test package",
        url="https://github.com/dosokin/ft_package",
        author="dosokin",
        author_email="<dosokin@student.42angouleme.fr>",
        license="MIT",
        package_dir={"": "base-ft_package"},
        packages=find_packages(where="base-ft_package"),
)