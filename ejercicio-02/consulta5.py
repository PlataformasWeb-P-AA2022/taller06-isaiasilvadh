from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
from genera_base import Pais 

engine = create_engine('sqlite:///paises.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

print("Presentación de todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'")
paises = session.query(Pais).filter(or_(Pais.nombre.like("%uador%"), Pais.capital.like("%ito%"))).order_by(Pais.capital).all()
print(paises)