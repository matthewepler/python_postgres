from src import app


TEST_FILE_CONTENT = """hello, world
hello, there"""


def test_read_file_to_list(tmpdir):
    directory = tmpdir.mkdir('data')
    tmp_file = directory.join('data.csv')
    tmp_file.write(TEST_FILE_CONTENT)

    str_list = app.file_to_list(f'{tmpdir}/data/data.csv')

    # with open(f'{tmpdir}/data/data.csv') as f:
    #     print(f.readlines())

    assert len(str_list) == 2
