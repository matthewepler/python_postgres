import click

from onboarding.resources.resource_types import resource_types
from onboarding.resources.resource import Resource


@click.group()
def main():
    pass


# a hash map of created resource objects
# in-memory only. how would this work in the real world?
# guess: create interface here with Store class (get, set, etc)
# and then can switch out but keep the interface...?
known_resources = set()


@main.command()
@click.argument('source')
@click.argument('target')
@click.option('--t_type',
              type=click.Choice([resource_types.keys()]))
@click.option('--s_type',
              type=click.Choice([resource_types.keys()]))
@click.option('--save',
              help='boolean, save source for later reference',
              default=False)
@click.option('--parser',
              type=click.File('r'),
              help=('optional file for parsing source data before'
                    'importing into a target Resource'))
def add_records(source,
                save,
                target,
                s_type=None,
                parser=None,
                t_type=None):

    """
    Imports data from a source to a target. Optionally provides ability
    to save sources for future use and to specify how to treat incoming data.

    Parameters:
        source (str): name of exisiting Resource or origin of
                        new Resource (path, etc - should match s_type)
        save (bool):  if True, saves the source in memory for later reference
        target (str): name of existing Resource or name to give to
                        new Resource
        s_name (str): optional name if saving with --save boolean flag.
                        if not set, the name will be auto-generated
        s_type (str): if creating a new Resource, specify the type.
                        Possible values can be found in `resoure_types.py`
        parser (str): optional file path to document that desribes how to
                        evaluate incoming data before importing to target
        t_type (str): if creating new target Resource, specify the type.
                        Possible values can be found in `resource_types.py`

    Returns:
        (int) 1
    """

    # fetch or create a source resource
    source = fetch_resource(source, s_type, save)

    # fetch or create a target resource
    target = fetch_resource(target, t_type)

    # import the source to the target (with parser)
    return 1


def fetch_resource(name: str, type_: str, save: bool) -> Resource:
    """
    Returns an existing Resource object if it exists. If not, a new
    Resource is created and optionally saved)

    Parameters:
        name (str):  name of existing Resource, or name to be
                       assigned to new Resource
        type_ (str): if creating new Resource, type of Resource to be
                       created. Possible values in `resource_types.py`
        save (bool): if True, new Resource will be saved

    Returns:
        resource (Resource): an instance of the Resource class
    """

    pass


def create_resource(type: str) -> Resource:
    resource = None
    try:
        resource = resource_types.get(type)
        known_resources.add((resource.name, resource))
    # ?? - thought I should put this `except` here for a more readable
    #      error message. Should I just use a simple return
    #      ala EAFP? `return resource_types.get(type) or None`
    except(KeyError):
        raise KeyError(f'Could not create a resource of type {type}')

    return resource


if __name__ == "__main__":
    main()
