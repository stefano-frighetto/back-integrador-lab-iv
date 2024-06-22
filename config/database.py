from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base
#x7I10Sh32DcA
DATABASE_URL = "mysql+mysqlconnector://root:CONTRASENIA@localhost:3306/bdd-integrador-lab-iv"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
