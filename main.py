#!/usr/bin/env python3

import click
from iterfzf import iterfzf
import transaction_rc as trc
from pathlib import Path


@click.group()
def cli():
    pass


@click.command()
@click.argument('file_name', default="")
def run(file_name):
    if file_name == '':
        file_name = fzf_select_transaction()
    click.echo('Calculating...')
    trc.parse_transaction_rc(file_name)


def fzf_select_transaction() -> str:
    result = iterfzf(trc.get_list_of_transaction_rcs())
    if not result:
        print('No transaction selected via args, and FZF selection interface failed!')
        exit(1)
    path = Path(result)
    return path


if __name__ == '__main__':
    cli.add_command(run)
    cli()
