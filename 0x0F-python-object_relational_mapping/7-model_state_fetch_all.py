#!/usr/bin/python3
""" Lists all the states in the table"""

if __name__ == "__main__":
    from model_state import State, Base
    from sqlalchemy import (create_engine, Table, Integer,
                            String, Column)
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], 
				sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sesh = sessionmaker()
    sesh.configure(bind=engine)
    session__ = sesh()

    for state in session__.query(State):
        print("{}: {}".format(state.id, state.name))
