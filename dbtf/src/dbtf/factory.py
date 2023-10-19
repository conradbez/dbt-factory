# %%
import click
import yaml
from pathlib import Path
from dbt.cli.main import dbtRunner, dbtRunnerResult
import sys
import os
import shutil
# PROJECT_DIR = Path("dbt_project")
PROJECT_DIR = Path(".")
TEMPLATE_DIR = Path("./templates")
DBT_RUN_ARGS = [
    "--profiles-dir", PROJECT_DIR, 
    "--project-dir", PROJECT_DIR # for now we assume this is current directory
    ]

def init():
    pkgdir = Path(sys.modules['dbtf'].__path__[0])
    try:
        shutil.copytree(pkgdir / "dbt_project", Path(os.getcwd())/ "dbt_project")
    except:
        print('project already exists')
    
# %%
# @click.command()
def generate_sources():
    # generate sources.yaml
    data_discovered = [f for f in (PROJECT_DIR / "seeds").iterdir() if f.is_file()]
    template = """
version: 2
sources:
  - name: test_duckdb
    schema: main_seed_data  
    tables:
    """
    for data_file in data_discovered:
        
        template += f"""
      - name: {data_file.stem}"""

    (PROJECT_DIR / "models" / "raw").mkdir(exist_ok=True)
    with open(PROJECT_DIR / "models" / "raw" /"sources.yml", "w") as f_out:
        f_out.write(template)

    # generates models for each of the sources so we don't have to use "source()" in our generated model code
    with open(PROJECT_DIR / 'models' / "raw" / 'sources.yml', 'r') as file:

        sources_yaml = yaml.safe_load(file)
        for source_dict in sources_yaml['sources']:
            for table_dict in source_dict['tables']:
                table_name = table_dict['name']
                source_line = f'''source("{source_dict['name']}", "{table_name}")'''
                jinja_source_line = "select * from {{" + source_line + "}}"
                file_name = table_name+".sql"
                with open(PROJECT_DIR / "models" / "raw" / file_name, "w") as f_out:
                    f_out.write(jinja_source_line)


# %%
# @click.command()
def generate_models():
    model_index = 0
    with open('factory_config.yml', 'r') as file:
        factory_config = yaml.safe_load(file)
    for model_name, model in factory_config['nodes'].items():
        model_string = open(TEMPLATE_DIR / (model['template']+'.sql'), "r").read()
        for dep_name, dep_value in model['dependencies'].items():
            model_string = model_string.replace(f'##{dep_name}##', f'"{dep_value}"')
    with open(PROJECT_DIR / "models" / ( str(model_index)+ '.' + model_name +'.sql'), "w") as f_out:
        f_out.write(model_string)

    model_index += 1

# %%
def run_dbt():
    generate_sources()
    generate_models()
    dbt = dbtRunner()

    res: dbtRunnerResult = dbt.invoke(["seed",*DBT_RUN_ARGS])
    # for r in res.result:
    #     print(r)

    # # run dbt
    res: dbtRunnerResult = dbt.invoke(["run", *DBT_RUN_ARGS])
    # for r in res.result:
    #     print(r)

    dbt.invoke(["clean",*DBT_RUN_ARGS])

if __name__ == "__main__":
    run_dbt()
