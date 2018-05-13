import os

import click

from oversee import terminal
from oversee import config


@click.group()
def main():
    pass


@click.command()
@click.argument('name')
def install(name):
    """Installs a module defined in the .yaml file. Options include: {}"""
    terminal.install(name)


@click.command()
@click.argument('src')
@click.argument('dst')
def move(src, dst):
    """Moves a file / folder from one location to another using scp!"""
    terminal.scp(src, dst)


@click.command()
@click.argument('name')
def export(name):
    """Exports your bash aliases to .bash_aliases!"""
    terminal.export_aliases(name)


@click.group()
def jetbrains():
    pass


@click.command()
@click.argument('name')
def save(name):
    name = name.lower()
    name = '.{}'.format(name)
    click.echo('saving {}'.format(name))

    paths = []
    for path in os.listdir(os.path.expanduser('~')):
        path = os.path.join(os.path.expanduser('~'), path)
        if os.path.isdir(path):
            folder = os.path.basename(path)
            folder = folder.lower()
            if folder.startswith(name):
                paths.append(path)

    if len(paths) == 0:
        click.echo('No paths matching {} found!'.format(name))
        return
    elif len(paths) > 1:
        click.echo('More than one path matching {} found!'.format(name))
        return
    else:
        path = paths[0]

    path = os.path.join(path, 'config')


jetbrains.add_command(save)


# noinspection PyUnresolvedReferences
install.help = install.__doc__.format(' '.join(config.install.keys()))

main.add_command(install)
main.add_command(move)
main.add_command(export)
main.add_command(jetbrains)


if __name__ == '__main__':
    main()
