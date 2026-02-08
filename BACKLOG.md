| Feature                                                            | Priority | Status |
| :----------------------------------------------------------------- | :------- | :----- |
| Move all cli commands to be under dbtf                             | Y        | Done   |
| Publish to PyPi                                                    | Y        | Done   |
| Upgrade to dbt-core 1.11+ and dbt-duckdb 1.10+                     | High     | Done   |
| Fix deprecation warnings (+ schema prefix)                         | High     | Done   |
|                                                                    |          |        |
| **Core Engine Improvements**                                       |          |        |
| Add YAML Validation (Pydantic/Schema)                              | High     |        |
| Layered Defaults (Default materialization/configs)                 | Med      |        |
| Refactor `PROJECT_DIR` for robust pathing                          | High     |        |
| Header tags for generated SQL (DO NOT EDIT)                        | Low      |        |
|                                                                    |          |        |
| **Functional Features**                                            |          |        |
| Pass user args to dbt                                              | Med      |        |
| Automagically parse dbt-utils and place them into templates        | N        |        |
| Add Alteryx feature complete templates                             | N        |        |
| Test on Python in browser (PyScript instructions)                  | Low      |        |
| Add explicit exceptions (missing project/invalid yaml)             | High     |        |
| Use dbt's logger for unified terminal output                       | Low      |        |
