import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'preprocess_arkerpay', # this should be unique
    version = '0.0.1',
    author = 'Jonathon Parker',
    author_email= 'arkerpay@fake.com',
    description = 'This is preprocessing package',
    long_description= long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'   ],
    python_requires = '>= 3.5'
)
