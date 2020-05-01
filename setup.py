from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name='htmldiff2',
    author='Ed Summers',
    author_email='ehs@pobox.com',
    version='0.1.1',
    url='https://github.com/edsu/htmldiff2',
    py_modules=['htmldiff2'],
    description='Diffs arbitrary HTML inline.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    install_requires=['genshi', "html5lib"],
    test_suite='test',
    python_requires=">=3.5",
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
