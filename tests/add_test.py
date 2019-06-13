import pytest

from records import add

TEST_FILE_CONTENT = """hello, world
hello, there"""


@pytest.fixture
def csv_fixture(tmpdir):
    directory = tmpdir.mkdir('data')
    tmp_file = directory.join('data.csv')
    tmp_file.write(TEST_FILE_CONTENT)
    yield tmp_file


def exits_if_args_not_valid():
    assert 1
