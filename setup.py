from setuptools import setup
setup(
    name='dynamic',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'dynamic=main:search_obj.search_args'
        ]
    }
)