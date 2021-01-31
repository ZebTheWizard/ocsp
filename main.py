import click
from app.ocsp import Ocsp
from app.helpers import *


@click.group()
def cli():
    pass


@click.command()
@click.option("--host", default="ocsp.apple.com", help="the hostname of the ocsp server")
@click.option("--port", default="443", help="the port of the ocsp server")
def root_cert(host, port):
    o = Ocsp(host, port)
    click.echo(o.getRootServerCert())


@click.command()
@click.option("--host", default="ocsp.apple.com", help="the hostname of the ocsp server")
@click.option("--port", default="443", help="the port of the ocsp server")
def chain(host, port):
    o = Ocsp(host, port)
    click.echo(o.getChainAsString())


@click.command()
@click.option("--host", default="ocsp.apple.com", help="the hostname of the ocsp server")
@click.option("--port", default="443", help="the port of the ocsp server")
def responder(host, port):
    o = Ocsp(host, port)
    click.echo(o.getResponderUrl())


if __name__ == '__main__':
    cli.add_command(root_cert)
    cli.add_command(chain)
    cli.add_command(responder)
    cli()
    removeAllTempFiles()
