from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
from genera_base import Pais 

engine = create_engine('sqlite:///paises.db')


Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

print("Presentación de todos los paises de Asia ordenados por el dial")
paises = session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()
print(paises)