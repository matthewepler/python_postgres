def file_to_list(f_path):
    with open(f_path, 'r') as f:
        return f.readlines()


# # generate database schema
# metadata.metadata.create_all(engine)

# # create new session
# session = Session()

# # create records
# game_one = Game([
#     ('source_id', 'abcdef'),
#     ('rated', False),
# ])

# # persist data
# session.add(game_one)

# session.commit()
# session.close()
