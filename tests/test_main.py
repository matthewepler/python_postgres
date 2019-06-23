from onboarding import main
from onboarding.resources.resource import Resource


# create a resource based on the source_type
def test_creates_resource_object():
    file_resource = main.create_resource('file')
    assert isinstance(file_resource, Resource)
