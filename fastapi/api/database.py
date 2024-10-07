from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Endereço do banco de dados
SQL_ALCHEMY_DATABASE_URL = 'sqlite:///workout.db'

# Cria um objeto engine em SQLAlchemy, biblioteca ORM em Python
# connect_args={'check_same_thread': False} permite que as conexões sejam usadas em diferentes threads
engine = create_engine(SQL_ALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
# Cria uma fábrica de sessões para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Cria uma classe base a partir da qual suas classes de modelo serão derivadas
Base = declarative_base()



