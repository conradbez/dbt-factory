import click

from dbtf.__about__ import __version__
from dbtf import factory

@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="dbtf")
def dbtf():
    click.echo("dbt-factory")


@dbtf.command()  # This decorator adds the 'run' function as a subcommand to the 'dbtf' group.
@click.option('--option_name', default="default_value", help='Run a dbt-factory project')
def run(option_name):
    """Run a dbt-factory project"""
    click.echo(f"Running with option: {option_name}")
    try:
        factory.run_dbt()
    except:
        print("Make sure you have run `dbtf init` and `cd`'d into the directory before running")

@dbtf.command()  # This decorator adds the 'init' function as a subcommand to the 'dbtf' group.
@click.option('--option_name', default="default_value", help='Initialize a blank dbt-factory project')
def init(option_name):
    """Initialize a blank dbt-factory project"""
    
    click.echo(f"Running with option: {option_name}")
    factory.init()

if __name__ == '__main__':
    dbtf()