import click
from grpcadmin.utils import create_service


@click.group()
def cli():
    """Helper for creation grpc services"""
    pass


@cli.command()
@click.argument('name')
def create(name):
    """Service for creating stub dirs service.

    \b
    Example:
        $grpc-admin create example.
        This command create dirs for service "example" with stub proto file for future filling"""
    create_service(name)


@cli.command()
@click.option('--name', '-n', multiple=True, type=click.STRING,
              help="Name of service will be compiled. It's multiple option. "
                   "If the option is missed all services will be compiled.")
@click.option('--except_for', '-e', multiple=True, type=click.STRING,
              help="Name of service won't be compiled. It's multiple option.")
def compile(name, except_for):
    """Service for compile proto files to python.
    Service get proto files from directory: <service_name>/proto_buf/ @TODO

    For compilation all proto files @TODO

    \b
    Example:
        $grpc-admin create example.
        This command create dirs for service "example" with stub proto file for future filling"""
    click.echo((name, except_for))


@cli.command()
@click.option('--adress', '-a', default='', type=click.STRING, help='adress')
@click.option('--max_workers', '-m', default=1, type=click.IntRange(min=1, max=128), help='number of workers')
@click.option('--protofile', '-p', multiple=True,
              type=click.STRING, help="Proto file. It's multiple option.")
def server(adress, max_workers, protofile):
    """comment"""
    click.echo(adress)
    click.echo(max_workers)
    click.echo(protofile)
