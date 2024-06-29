from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base
# contraseña stefano
#x7I10Sh32DcA
DATABASE_URL = "mysql+mysqlconnector://root:dona0903@localhost:3306/integradorLabIV"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
