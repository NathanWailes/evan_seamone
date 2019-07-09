# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = download_cases.settings']},
    package_data = {
        'download_cases': [
            'citation_numbers.csv'
        ]
    },
    zip_safe=False,
)
