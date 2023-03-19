from dagster import asset
import pandas as pd
import polars as pl
from polars import DataFrame
from duckdb import sql


@asset
def population() -> DataFrame:
    df = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    )[0]
    columns = [
        "country",
        "continent",
        "subregion",
        "population_2018",
        "population_2019",
        "pop_change",
    ]
    population_df = pl.DataFrame(df, columns=columns)
    population_df = (
        population_df
        .with_columns(pl.col("pop_change").str.rstrip("%").str.replace("\u2212", "-").cast(float))
    )
    return population_df


@asset
def continent_population(population: DataFrame):
    df = sql("select continent, avg(pop_change) as avg_pop_change from population group by 1 order by 2 desc").pl()
    df.write_csv('try.csv', has_header=True)
