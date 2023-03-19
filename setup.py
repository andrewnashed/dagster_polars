from setuptools import find_packages, setup

setup(
    name="jkk",
    packages=find_packages(exclude=["population_pipeline_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "polars",
        "pandas",
        "sqlescapy",
        "lxml",
        "html5lib",
        "duckdb"
    ],
    extras_require={"dev": ["dagit", "pytest", "localstack", "awscli-local", "awscli"]},
)
