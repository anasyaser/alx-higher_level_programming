#!/usr/bin/python3
"""
Script that prints the first State object from the database
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
    is_match = session.query(State).filter(State.name == argv[4])
    if is_match:
        print(is_match.id)
    else:
        print("Not found")
    session.close()
