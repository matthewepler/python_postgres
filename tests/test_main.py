import pytest

from src import app


TEST_FILE_CONTENT = """hello, world
hello, there"""


@pytest.fixture
def csv_fixture(tmpdir):
    directory = tmpdir.mkdir('data')
    tmp_file = directory.join('data.csv')
    tmp_file.write(TEST_FILE_CONTENT)
    yield tmp_file


def test_read_file_to_list(csv_fixture):
    str_list = app.file_to_list(csv_fixture)
    assert len(str_list) == 2


def test_row_to_dict():
    headers = ['a', 'b', 'c']
    row = [1, 2, 3]

    result = app.row_to_zip(headers, row)

    assert type(result) is zip
