from datetime import datetime


def parse_datetime(stamp: str):
    stamp = int(float(stamp))
    try:
        result = datetime.fromtimestamp(stamp/1000)
    except ValueError:
        print(f'could not coerce {stamp} to datetime object')
        raise
    return result


parser_defs = {
    'id': lambda x: str(x),
    'rated': lambda x: x.lower() == 'true',
    'created_at': parse_datetime,
    'last_move_at': parse_datetime,
    'turns': lambda x: int(x),
    'victory_status': lambda x: str(x),
    'winner': lambda x: str(x),
    'increment_code': lambda x: str(x),
    'white_id': lambda x: str(x),
    'white_rating': lambda x: int(x),
    'black_id': lambda x: str(x),
    'black_rating': lambda x: int(x),
    'moves': lambda x: str(x),
    'opening_eco': lambda x: str(x),
    'opening_name': lambda x: str(x),
    'opening_ply': lambda x: int(x)
}
