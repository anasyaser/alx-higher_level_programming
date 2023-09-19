#!/usr/bin/python3
"""
Script that search for given name
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    is_match = session.query(State).filter(State.name == sys.argv[4]).first()
    if is_match:
        print("{}".format(is_match.id))
    else:
        print("Not found")
    session.close()
