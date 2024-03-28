from setuptools import setup, find_packages

setup(
    name='genlit',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-SQLAlchemy',
        'psycopg2-binary'
    ],
    entry_points={
        'console_scripts': [
            'genlit=genlit.app:main',  # This line assumes you have a main function in app.py that serves as the entry point to your application
        ],
    },
)
