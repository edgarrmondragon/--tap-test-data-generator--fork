#!/usr/bin/env python
from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


test_deps = [
    "pytest==6.2.2",
    "pytest-cov==2.11.1",
    "pytest-mock==1.10.0",
    "testfixtures==6.3.0",
    "coverage==5.5"
]
extras = {
    'test': test_deps,
}
setup(
    name="tap-test-data-generator",
    version="1.2.0",
    description="Singer.io tap for generating test data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ericlebail",
    url="https://github.com/ericlebail/tap-test-data-generator",
    classifiers=["Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent"],
    py_modules=["tap_test_data_generator"],
    install_requires=[
        "singer-python==5.12.1",
        "requests",
        "jsonschema==2.6.0",
        "Faker==7.0.1",
        "exrex==0.10.5",
        "ijson==3.1.4",
        "allpairspy==2.5.0"
    ],
    tests_require=test_deps,
    extras_require=extras,
    entry_points="""
    [console_scripts]
    tap-test-data-generator=tap_test_data_generator:main
    """,
    packages=find_packages(),
    package_data={
        "schemas": ["tap_test_data_generator/schemas/*.json"],
        "metadatas": ["tap_test_data_generator/metadatas/*.json"],
        "object-repositories": ["include tap_test_data_generator/object-repositories/*.json"],
        "sample-config": ["sample_config.json"]
    },
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False
)
