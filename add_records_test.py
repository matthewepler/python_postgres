import pytest

import add_records


TEST_FILE_CONTENT = """hello, world
hello, there"""


@pytest.fixture
def csv_fixture(tmpdir):
    directory = tmpdir.mkdir('data')
    tmp_file = directory.join('data.csv')
    tmp_file.write(TEST_FILE_CONTENT)
    yield tmp_file


def test_takes_two_args():
    with pytest.raises(ValueError):
        add_records.main()