import click
import grpcadmin
from click_plugins import with_plugins
from pkg_resources import iter_entry_points


@with_plugins(iter_entry_points('grpcadmin.plugins'))
@click.group()
def cli():
    """
    TEXT
    \b
    SOME_TEXT:
    \b
        $ cat
    """


@cli.command()
@click.argument('a', type=click.STRING, default='')
def create(a):
    print(grpcadmin.joke())
    print(a)


@cli.command()
@click.argument('a', type=click.STRING, default='')
def compile(a):
    print(grpcadmin.joke())
    print(a)