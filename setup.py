from setuptools import setup
import sdist_upip

with open("README.MD", "r") as long_description_file_reader:
    long_description = long_description_file_reader.read()

setup(
    name='micropython-picowebrouter',
    version="v0.1.1",
    description="Pi Pico webserver",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MikeSchapp/PicoWebRouter',
    author='MikeSchapp',
    keywords='micropython, webserver',
    project_urls={
        'Source': 'https://github.com/MikeSchapp/PicoWebRouter',
    },
    license='BSD 2',
    packages=['picowebrouter', 'picowebrouter/objects'],
    cmdclass={'sdist': sdist_upip.sdist}
)

