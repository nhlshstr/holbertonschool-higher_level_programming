#!/usr/bin/python3
"""lists all the states in the table"""

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
   
    found_state_i = (session__.query(State)
            .order_by(State.id).filter(State.name == sys.argv[4]).first())
    if found_state_i is None:
        print("Not found")
    else:
        print("{}".format(found_state_i.id))
