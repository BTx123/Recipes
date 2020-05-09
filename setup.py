from setuptools import setup

setup(
    name="make_recipe",
    version="0.1",
    py_modules=["make_recipe"],
    install_requires=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        make_recipe=make_recipe:main
    ''',
)
