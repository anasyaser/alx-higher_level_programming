#!/usr/bin/python3
"""
Fetch all recorder that conatain letter 'a'
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
    query = session.query(State).filter(State.name.ilike('%a%')).order_by(
        State.id).all
    for row in query:
        print("{}: {}".format(row.id, row.name))
    session.close()
