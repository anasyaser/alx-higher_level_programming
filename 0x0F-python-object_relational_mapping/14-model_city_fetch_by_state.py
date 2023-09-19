#!/usr/bin/python3
"""
Script that print all citites and its state name
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    query = session.query(State).join(City).order_by(City.id).all()
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
