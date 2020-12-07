from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.1.2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'Flask-SQLAlchemy'
    ],
)