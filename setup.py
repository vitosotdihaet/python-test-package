from setuptools import setup, find_packages

setup(
    name='python_test_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Vitaly Klimenko',
    author_email='vitostikitos@gmail.com',
    description='A simple greeting library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vitosotdihaet/python-test-package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
