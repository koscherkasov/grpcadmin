import click
from grpcadmin.utils import create_service


@click.group()
def cli():
    """Helper for creation grpc services"""
    pass


@cli.command()
@click.argument('name')
def create(name):
    """create service"""
    create_service(name)


@cli.command()
@click.option('--name', default='', type=click.STRING, help='name of service')
# @click.argument('name', default='', type=click.STRING)
def compile(name):
    """compile service"""
    click.echo(name)


@cli.command()
@click.option('--adress', default='', type=click.STRING, help='adress')
@click.option('--max_workers', default=1, type=click.IntRange(min=1, max=1024), help='number of workers')
@click.option('--protofiles', default='', type=click.STRING, help='comma separated protofiles')
def server(adress, max_workers, protofiles):
    """comment"""
    click.echo(adress)
    click.echo(max_workers)
    click.echo(protofiles)
