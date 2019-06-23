import click

from onboarding.resources.resource import Resource
from onboarding.resources.file_resource import FileResource


@click.group()
def main():
    pass


resource_types = {
    'file': FileResource()
}


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


def create_resource(type: str) -> Resource:
    resource = None
    try:
        resource = resource_types.get(type)
    # ?? - thought I should put this here for a more readable
    #      error message. Should I just use a simple return
    #      ala EAFP? return resource_types.get(type) or None
    except(KeyError):
        raise KeyError(f'Could not create a resource of type {type}')

    return resource


if __name__ == "__main__":
    main()
