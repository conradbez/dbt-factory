# dbt-factory

Write re-usable sql code blocks and compile to a dbt project through yaml configuration to improve data logic DRY-ness

If you're unfamiliar with (dbt)[https://github.com/dbt-labs/dbt-core], it is the leading sql data wrangling toolset (IMO) which adds really nice features and code modularity on top of SQL. `dbt-factory` aims to abstract dbt another level to increase DRYness and automatibility

**Table of Contents**

- [dbt-factory](#dbt-factory)
- [Usage](#usage)
  - [Installation](#installation)
  - [Inital setup](#inital-setup)
  - [How to add custom logic](#how-to-add-custom-logic)
- [Benefits](#benefits)
- [Details](#details)
  - [License](#license)


# Usage

## Installation

```console
pip install dbtf dbt-core==1.6.6 dbt-duckdb==1.6.1 dbt-core==1.6.6
```

## Inital setup

Create a blank dbt-factory project:

`dbtf init`

Run: 

`cd dbt_project`
`dbtf run`

## How to add custom logic

1. Add templates into `dbt_project/templates` using `##` as templating string (i.e. `##table_2##` will replace table_2 in `factory_config.yml`)

2. Add logic into `dbt_project/factory_config.yml`, i.e.:

```
nodes:
  test_append:
    template: append
    dependencies:
      table_1: test_table_1
      table_2: test_table_2
```

Which uses the template `template/append.sql` and replaces `table_1` and `table_2` in the template

3. Add data into `dbt_project/seeds`

4. Run `dbtf run`


# Benefits

- Construct pipeline without knowing SQL
- Construct pipelines without learning dbt
- Avoid duplicative code
- Easier automation of pipeline creation, so your code can interact with yaml instead of sql (advanced users)


Inspired by Airflow's [DAG Factory](https://github.com/ajbosco/dag-factory)



# Details

[![PyPI - Version](https://img.shields.io/pypi/v/dbtf.svg)](https://pypi.org/project/dbtf)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dbtf.svg)](https://pypi.org/project/dbtf)

-----

## License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/conradbez/dbt-factory">dbt-factory</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://conradbezuidenhout.com">Conrad Bezuidenhout</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>