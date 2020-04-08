import os
import click
from app import create_app


@click.group()
def cli():
    pass


@cli.command()
def run():
    """Run development server"""
    app = create_app(os.environ.get('RASTUCHKA_CONFIG'))
    app.run()


if __name__ == '__main__':
    cli()
