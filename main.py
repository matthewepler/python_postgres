import click


@click.group()
def main():
    pass


@main.command()
@click.argument('source_type', type=click.Choice(['file']))
@click.argument('target')
@click.option('--source', type=click.Path(exists=True, readable=True))
@click.option('--parser', type=click.File('r'))
def add_records(source_type, target, source=None, parser=None):
    # create a source resource
    # create a target resource
    # import the source to the target (with parser)
    return 1


@main.command()
def blah():
    click.echo('blah blah')


if __name__ == "__main__":
    main()
