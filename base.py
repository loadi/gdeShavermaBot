from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///places.db?check_same_thread=False', echo=False)
Base = declarative_base()


class Places(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    picture = Column(String)
    city = Column(String)
    commentsCount = Column(Integer)
    ratesCount = Column(Integer)
    rate = Column(Float)
    visits = Column(Integer)

    def __init__(self, id, name, description, picture, city, commentsCount, ratesCount, rate, visits):
        self.id = id
        self.name = name
        self.description = description
        self.picture = picture
        self.city = city
        self.commentsCount = commentsCount
        self.ratesCount = ratesCount
        self.rate = rate
        self.visits = visits


def addPlace(id, name, description, picture, city, commentsCount, ratesCount, rate, visits, attemps=0):
    try:
        session = Session(bind=engine)
        line = Places(id, name, description, picture, city, commentsCount, ratesCount, rate, visits)
        session.add(line)
        session.commit()
        session.close()

    except Exception as e:
        if attemps <= 3:
            attemps += 1
            addPlace(id, name, description, picture, city, commentsCount, ratesCount, rate, visits, attemps)
        else:
            print(e)
            input()


def searchPlace(name):
    session = Session(bind=engine)
    places = session.query(Places).filter(Places.name.like(f"{name}%")).all()
    return places


def searchPlaceByCity(places, city):
    ans = []
    for place in places:
        if place.city == city:
            ans.append(place)
    return ans


Base.metadata.create_all(engine)
