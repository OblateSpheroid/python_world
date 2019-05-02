from distutils.core import setup

setup(
    name="python_world",
    version="0.0.1",
    packages = ['python_world'],
    author="Cedd Burge",
    author_email="ceddlyburge@gmail.com",
    description="A function that returns 'world'",
    url="https://github.com/ceddlyburge/python_world",
    install_requires = ['numpy', 'pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

# pip install git+https://github.com/OblateSpheroid/python_world#egg=python_world
# python setup.py sdist --format gztar
